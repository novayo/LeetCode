class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        2,2,6
        '''
        if len(s) == 1:
            return 1 if s[0] != '0' else 0
        
        dp = [0] * len(s)
        
        # init
        if s[0] != '0':
            dp[0] = 1
        
            if s[1] != '0':
                dp[1] = 1
            
            if int(s[:2]) <= 26:
                dp[1] += 1
        
        for i in range(2, len(s)):
            
            if s[i] != '0':
                dp[i] += dp[i-1]
            
            if s[i-1] != '0' and int(s[i-1]+s[i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
