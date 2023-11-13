class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        edge = [["" for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 0
            for j in range(i+1, n):
                if s[i] == s[j] and i + 1 == j:
                    dp[i][j] = dp[i+1][j-1] + 2
                    edge[i][j] = s[i]
                elif s[i] == s[j] and (s[i] != edge[i+1][j-1]):
                    dp[i][j] = dp[i+1][j-1] + 2
                    edge[i][j] = s[i]
                else:
                    if dp[i+1][j] >= dp[i][j-1]:
                        dp[i][j] = dp[i+1][j]
                        edge[i][j] = edge[i+1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
                        edge[i][j] = edge[i][j-1]

        return dp[0][n-1]

