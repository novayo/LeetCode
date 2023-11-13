class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] => i~j是否是回文
        #   - 如果s[i]==s[j] => dp[i][j] = dp[i+1][j-1] + 2
        #   - 反之 => dp[i][j] = 之前的結果 = max(dp[i+1][j], dp[i][j-1])
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]

        
