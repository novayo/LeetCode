lass Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        dp = [[0] * 4 for _ in range(n+1)]

        for i in range(n, -1, -1):
            for prev_choice in range(2, -2, -1):
                if i == n:
                    dp[i][prev_choice] = 0
                    continue
                
                ans = float('inf')
                for j in range(3):
                    if j == prev_choice:
                        continue
                    ans = min(ans, costs[i][j] + dp[i+1][j])
                
                dp[i][prev_choice] = ans
        
        return dp[0][-1]
