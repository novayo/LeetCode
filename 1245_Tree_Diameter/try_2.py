class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        ans = 0
        colored = set()
        def recr(node):
            nonlocal ans
            
            if all([x in colored for x in graph[node]]):
                return 1
            
            min_heap = []
            for child in graph[node]:
                if child not in colored:
                    colored.add(child)
                    heapq.heappush(min_heap, recr(child))
                    if len(min_heap) > 2:
                        heapq.heappop(min_heap)
                    colored.remove(child)
            
            ans = max(ans, sum(min_heap))
            return max(min_heap) + 1
        
        colored.add(0)
        recr(0)
        return ans