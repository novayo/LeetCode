class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        
        for _n in range(2, n+1):
            i, j = 1, _n-1
            
            max_value = 0
            while i <= j:
                max_value = max(max_value, max(i, dp[i]) * max(j, dp[j]))
                i, j = i+1, j-1
            
            dp[_n] = max_value
        
        return dp[-1]