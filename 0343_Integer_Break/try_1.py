class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        
        for _n in range(3, n+1):
            i = 1
            j = _n-1
            max_product = 0
            
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                i += 1
                j -= 1
            
            dp[_n] = max_product
        
        return dp[n]
            