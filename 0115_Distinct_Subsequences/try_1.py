class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * n for _ in range(m)]

        # init => 第一行不用看上一行
        cur = 0
        for j in range(n-1, -1, -1):
            if s[j]==t[-1]:
                cur += 1
            dp[0][j] = cur

        # 第二行開始要去看上一行
        for i in range(1, m):
            # 從倒數第二個開始往前計算即可
            same = t[m-i-1] 
            for j in range(n-i-1, -1, -1):
            
                # 如果與之相等，則需計算此b跟it的組合 + 之前bit的組合個數
                if s[j] == same:
                    dp[i][j] = dp[i-1][j+1] + dp[i][j+1]
                # 若不相等，則維持之前bit的組合個數
                else:
                    dp[i][j] = dp[i][j+1]

        return dp[m-1][0]