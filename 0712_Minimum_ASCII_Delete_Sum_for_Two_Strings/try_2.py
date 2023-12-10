class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j] = s1[i:] & s2[j:]的最小刪除值
        #    - if s1[i] != s2[j] => dp[i][j] = min(刪除s1[i] + dp[i+1][j], 刪除s2[j] + dp[i][j+1])
        #    - if s1[i] == s2[j] => dp[i][j] = dp[i+1][j+1]
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # init
        #    - s2是空的，刪掉每個s1
        for i in range(m-1, -1, -1):
            dp[i][n] = dp[i+1][n] + ord(s1[i])
        
        #   - s1是空的，刪掉每個s2
        for j in range(n-1, -1, -1):
            dp[m][j] = dp[m][j+1] + ord(s2[j])
        
        # 取得答案
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1 ,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        
        return dp[0][0]
        
