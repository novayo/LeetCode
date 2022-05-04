class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9+7
        graph = collections.defaultdict(list)
        
        for a, b, cost in edges:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        
        hq = [(0, n)]
        cache = {}
        dp = [0] * (n+1)
        dp[n] = 1
        
        while hq:
            dist, node = heapq.heappop(hq)
            
            if node in cache:
                continue
            
            cache[node] = dist
            for nei, cost in graph[node]:
                if nei in cache and cache[node] > cache[nei]:
                    dp[node] += dp[nei]
                    dp[node] %= MOD
                
                if nei in cache:
                    continue
                
                heapq.heappush(hq, (dist + cost, nei))
            
            # 題目要求: node1要最大，所以在node1之後拜訪的點一定都比node1大，那這個時候就可以停止了
            if node == 1:
                break
        
        return dp[1]