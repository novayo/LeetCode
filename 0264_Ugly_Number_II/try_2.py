class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        cur_a = cur_b = cur_c = 0
        
        for i in range(1, n):
            dp[i] = min(dp[cur_a]*2, dp[cur_b]*3, dp[cur_c]*5)
            
            if dp[i] == dp[cur_a]*2:
                cur_a += 1
            
            if dp[i] == dp[cur_b]*3:
                cur_b += 1
            
            if dp[i] == dp[cur_c]*5:
                cur_c += 1
        
        return dp[-1]