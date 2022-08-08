class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in roads:
            graph[u].append((t, v))
            graph[v].append((t, u))
        
        
        MOD = 10**9+7
        dist = [float('inf')] * n
        ways = [1] * n
        dist[0] = 0
        pq = [(0, 0)] # cur_time, n
        
        while pq:
            time, node = heapq.heappop(pq)
            
            if dist[node] < time:
                continue
            
            for t, nei in graph[node]:
                if dist[nei] > time + t:
                    dist[nei] = time+t
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (time+t, nei))
                elif dist[nei] == time + t:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n-1]
