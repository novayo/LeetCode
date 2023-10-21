class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        
        for integer in range(1, n):
            for val in range(1, n+1):
                if integer > val:
                    continue
                
                dp[val] = max(dp[val], dp[val-integer] * integer)
        return dp[n]
        
