class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n+1)
        
        for i in range(n+1):
            if i <= 1:
                dp[i] = i
                continue
            elif i == 2:
                dp[i] = 1
                continue
            
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]
