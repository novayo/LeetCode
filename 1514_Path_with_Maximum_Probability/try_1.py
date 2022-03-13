class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        
        cache = set()
        heap = [(-1, start)]
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob *= -1
            
            if node == end:
                return prob
            
            if node in cache:
                continue
            cache.add(node)
            
            for nei, nei_prob in graph[node]:
                if nei in cache:
                    continue
                
                heapq.heappush(heap, (-prob*nei_prob, nei))
        
        return 0