class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        
        ans = 0
        # init
        for i in range(n):
            dp[i][i] = 1
            ans += 1 
        
        # loop
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    ans += 1
        
        return ans
