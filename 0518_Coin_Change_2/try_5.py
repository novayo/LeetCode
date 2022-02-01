class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        dp[i][j] = 用前i個組成j 有幾種
        '''
        
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        
        for i in range(1+len(coins)):
            dp[i][0] = 1
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        
        return dp[len(coins)][amount]
        
