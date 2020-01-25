class Solution:
    def confusingNumber(self, N: int) -> bool:
        dp = {'0':0,'1':1,'6':9,'8':8,'9':6}
        
        ans=0
        for i, s in enumerate(str(N)):
            if s in dp:
                ans += dp[s]*(10**i)
            else:
                return False
        
        return ans != N
