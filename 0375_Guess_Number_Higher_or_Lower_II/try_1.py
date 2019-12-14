class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp
        import numpy as np
        dp = np.zeros((n+1,n+1))
        
        def recur(i, j):
            if i>=j: return 0
            if dp[i][j] != 0:
                return dp[i][j]   
            
            dp[i][j] = float('inf')
            for k in range((i+j)//2, j):
                dp[i][j] = min(dp[i][j], k + max(recur(i, k - 1), recur(k + 1, j)))
                # print(i, k, j, dp[i][j])
            
            return dp[i][j]
        
        return int(recur(1, n))
