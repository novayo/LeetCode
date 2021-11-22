class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        dp = [[float('inf')] * (amount+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 0
        
        for j in range(1, amount+1):
            for i in range(1, m+1):
                coin = coins[i-1]
                
                if j >= coin and dp[i][j-coin] != float('inf'):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coin] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
                
        
        return dp[m][amount] if dp[m][amount] != float('inf') else -1
