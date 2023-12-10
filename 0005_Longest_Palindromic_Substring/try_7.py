class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = palindrone
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            
        ans = s[0]
        for length in range(2, n+1):
            for j in range(length-1, n):
                i = j-length+1
                if s[i] == s[j] and (i+1 == j or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j-i+1 > len(ans)):
                        ans = s[i:j+1]
                else:
                    dp[i][j] = False
        
        return ans
        
