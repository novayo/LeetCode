class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s == None or len(s) == 0):
            return s
        res = ""
        dp = [[False] * len(s) for i in range(len(s))]
        maxn = 0
        for j in range(0, len(s)):
            for i in range(0, j+1):
                dp[i][j] = ((s[i] == s[j]) and ((j-i<=2) or dp[i+1][j-1]))
                if (dp[i][j]):
                    if (j-i+1 > maxn):
                        maxn = j - i + 1
                        res = s[i:j+1]
        
        return res
        
