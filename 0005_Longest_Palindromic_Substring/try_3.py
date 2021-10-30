class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        cur_max = 1
        ans = [0, 0]
        
        # init
        for i in range(n):
            dp[i][i] = True
        
        # loop
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                length = j-i+1
                if s[i] == s[j] and (length <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                
                    if length > cur_max:
                        cur_max = length
                        ans[0], ans[1] = i, j

        return s[ans[0]:ans[1]+1]
