class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        
        dp = [0] * (n+1)
        
        # init
        for i in range(2, n+1):
            dp[i] = i
        
        # copy
        for i in range(2, n+1):
            for j in range(i*2, n+1, i):
                dp[j] = min(dp[j], dp[i] + 1 + ((j-i) // i))
        
        return dp[n]
