class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp
        dp = {}
        
        def recur(i, j):
            if i>=j: return 0
            if (i, j) in dp:
                return dp[i, j]
            
            dp[i, j] = float('inf')
            for k in range((i+j)//2, j):
                left, right = recur(i, k - 1), recur(k + 1, j)
                dp[i, j] = min(dp[i, j], k + max(left, right))
                if left > right: break
                
            return dp[i, j]
        
        return int(recur(1, n))
