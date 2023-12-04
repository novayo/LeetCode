class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n1, n2 = len(text1), len(text2)
        dp = [0] * (n2+1)
        
        for i in range(n1-1, -1, -1):
            prev_right = [0] * (n2+1)
            for j in range(n2-1, -1, -1):
                prev_right[j] = dp[j]
                dp[j] = max(
                    prev_right[j+1] + int(text1[i] == text2[j]),
                    dp[j+1],
                    dp[j]
                )
                
        return dp[0]

