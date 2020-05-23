class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s)+1)
        dp[0] = dp[1] = 1
        for i in range(2, len(dp)):
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            
            if s[i-2] == '1' or (0 < int(s[i-2]) <= 2 and int(s[i-1]) <= 6):
                dp[i] += dp[i-2]

        return dp[-1]
