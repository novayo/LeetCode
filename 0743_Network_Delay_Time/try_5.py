class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, time in times:
            graph[a].append((b, time))
        
        pq = [(0, k)] # time, node
        visited = set()
        
        while pq:
            time, node = heapq.heappop(pq)
            
            visited.add(node)
            
            if len(visited) == n:
                return time
            
            for nei, t in graph[node]:
                if nei in visited:
                    continue
                heapq.heappush(pq, (time + t, nei))
            
        return -1
            
