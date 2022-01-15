class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for i, j, w in times:
            graph[i].append((w, j))
        
        # build table
        table = [0]
        for i in range(1, n+1):
            table.append(float('inf'))
        
        # dijkstra
        heap = [(0, k)]
        while heap:
            w_node, node = heapq.heappop(heap)
            
            # 沒走過的話
            if table[node] < float('inf'):
                continue
            table[node] = w_node
            
            for w_nei, nei in graph.get(node, []):
                # 沒走過的話
                if table[nei] == float('inf'):
                    heapq.heappush(heap, (w_node+w_nei, nei))
        
        _max = max(table)
        return _max if _max != float('inf') else -1
