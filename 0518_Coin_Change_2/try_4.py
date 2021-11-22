class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        dp[i][j] = 取前i個，組成amount(0~amount) 的 個數
        
        dp[i][j] = dp[i-1][j] + dp[i][j-coin]
        '''
        m = len(coins)
        dp = [[0] * (amount+1) for _ in range(m+1)]
        
        # init
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, amount+1):
                c = coins[i-1]
                
                dp[i][j] = dp[i-1][j]
                if j >= c:
                    dp[i][j] += dp[i][j-c]
        
        return dp[m][amount]
