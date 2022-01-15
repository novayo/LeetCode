class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for i, j, w in times:
            graph[i].append((w, j))
        
        # build table
        table = [0]
        for i in range(1, n+1):
            table.append(0 if i == k else float('inf'))
        
        # bellman ford
        old_table = []
        while not self.same_list(old_table, table):
            old_table = table.copy()
            for node in range(1, n+1):
                for w_nei, nei in graph.get(node, []):
                    if table[nei] > table[node]+w_nei:
                        table[nei] = table[node]+w_nei
        
        _max = max(table)
        return _max if _max != float('inf') else -1
    
    def same_list(self, list1, list2):
        if len(list1) != len(list2):
            return False
        for v1, v2 in zip(list1, list2):
            if v1 != v2:
                return False
        return True
