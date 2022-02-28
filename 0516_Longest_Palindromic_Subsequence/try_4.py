class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        (x)bottom-up回來之後，去添加所有可能，並計算答案
        如果i-1==j+1 => i~j看是不是回文，如果是，則i-1~j+1也是
        '''
        n = len(s)
        ans = 0
        
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1, -1, -1):
            j = n
            for k in range(i):
                i, j = i-1, j-1
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
