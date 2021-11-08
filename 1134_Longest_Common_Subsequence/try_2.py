class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        i for text1
        j for text2
        
        dp[i][j] = text1[:i] & text2[:j] 有幾個相同
        '''
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n) for i in range(m)]
        
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        
        # init
        for i in range(1, m):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        
        for j in range(1, n):
            if text2[j] == text1[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]
        
        # loop
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        
