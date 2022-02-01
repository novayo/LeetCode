class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        dp = [[float('inf')] * (amount+1) for _ in range(n+1)]
        
        # init
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                
                if j == coins[i-1]:
                    dp[i][j] = 1
                elif j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        
        return dp[n][amount] if dp[n][amount] < float('inf') else -1
