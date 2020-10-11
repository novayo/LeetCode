class Solution:
    def numTrees(self, n: int) -> int:
        '''
        
        '''
        dp = {0:1}
        def recr(n):
            
            if n in dp:
                return dp[n]
            
            ret = 0
            for i in range(n):
                ret += recr(i) * recr(n-i-1)
            dp[n] = ret
            return dp[n]
        
        return recr(n)    