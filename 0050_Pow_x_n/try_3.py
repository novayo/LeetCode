class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        recursion: top-down non-tail dp
        '''
        
        isNev = True if n < 0 else False
        n = -n if isNev else n
        
        dp = {0: 1, 1: x}
        
        def recr(x, n):
            
            if n not in dp:
                if n%2 == 0:
                    dp[n] = recr(x, n//2) * recr(x, n//2)
                else:
                    dp[n] = recr(x, n//2) * recr(x, n//2) * recr(x, 1)
                
            return dp[n]
        
        ret = recr(x, n)
        return 1/ret if isNev else ret