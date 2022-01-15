class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        dfs
        '''
        # build graph
        graph = collections.defaultdict(list)
        for node1, node2, weight in times:
            graph[node1].append((weight, node2))
        
        found = {}
        for i in range(1, n+1):
            found[i] = float('inf')
        
        def dfs(node, time):
            nonlocal found
            
            if found[node] <= time:
                return
            
            found[node] = time
            
            for weight, neighbor in sorted(graph[node]):
                dfs(neighbor, time+weight)
            
        dfs(k, 0)
        _max = max(found.values())
        return _max if _max != float('inf') else -1
