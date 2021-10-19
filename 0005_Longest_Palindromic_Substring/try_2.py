class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''
        dp = [[False] * n for _ in range(n)]
        
        for i in range(len(s)):
            dp[i][i] = True
            ans = s[i]
        
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j] and (j-i+1 <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > len(ans):
                        ans = s[i:j+1]
        
        return ans