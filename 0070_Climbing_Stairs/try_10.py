class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        
        for val in range(n+1):
            for step in [1, 2]:
                if step > val:
                    continue
                dp[val] += dp[val - step]
        return dp[n]
        
