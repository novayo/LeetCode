class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs) // 2
        
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0
        
        for a in range(n+1):
            for b in range(n+1):
                if a > 0:
                    dp[a][b] = min(dp[a][b], costs[a+b-1][0] + dp[a-1][b])
                if b > 0:
                    dp[a][b] = min(dp[a][b], costs[a+b-1][1] + dp[a][b-1])
        return dp[n][n]
