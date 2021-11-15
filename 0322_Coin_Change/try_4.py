class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[i][j] = 只使用前i種硬幣，組成j的話 = 最少k種
        
        dp[i][0] = 0
        dp[0][j] = 0
        
        if j - coins[i-1] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        else:
            dp[i][j] = dp[i-1][j]
        
        return dp[len(coin)][amount]
        '''
        n = len(coins)
        dp = [[float('inf')] * (amount+1) for _ in range(n+1)]
        
        # init
        for i in range(n+1):
            dp[i][0] = 0
        # for j in range(amount+1):
        #     dp[0][j] = 0
        
        # loop
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][amount] if dp[n][amount] != float('inf') else -1
