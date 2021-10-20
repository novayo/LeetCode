class Solution:
    def climbStairs(self, n: int) -> int:
        coins = [1, 2]
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for cur in range(2, n+1):
            for coin in coins:
                if cur - coin >= 0:
                    dp[cur] += dp[cur - coin]
        
        return dp[n]