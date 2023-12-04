class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                dp[i][j] = max(
                    dp[i+1][j+1] + int(text1[i] == text2[j]),
                    dp[i][j+1],
                    dp[i+1][j]
                )
        return dp[0][0]

