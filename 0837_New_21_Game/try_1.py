class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or k-1+maxPts<=n:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        
        i = 0
        cur_sum = 1
        for j in range(1, n+1):
            dp[j] = cur_sum / maxPts
            
            if j < k:
                cur_sum += dp[j]
            if j-i >= maxPts:
                cur_sum -= dp[i] 
                i += 1
            
        return sum(dp[k:])