class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        
        dp = [[0] * (n+1) for i in range(m+1)]
        
        # init
        # 因為dp[i][j]的意思是 s1[i:] 跟 s2[j:] 的最小刪除 => 所以底層要先初始化 => s1[m:]='' 要變成 s2[j:] j=n~0
        for i in range(m-1, -1, -1):
            dp[i][-1] = dp[i+1][-1] + ord(s1[i])
        
        for j in range(n-1, -1, -1):
            dp[-1][j] = dp[-1][j+1] + ord(s2[j])
        
        # loop
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        
        return dp[0][0]