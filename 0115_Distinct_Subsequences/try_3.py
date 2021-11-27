class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        定義：
            dp[i][j] = s[:i]與t[:j] '到目前為止' 有幾個相同
        
        初始化：
            ##############
            # 這是合理的 => s[:0] == t[:0] 的相同個數=1個
            dp[0][0] = 1 
            
            # 但是還沒初始化完
            dp[1][0] = 1 => 雖然s[1]!=t[0]，但到目前為止 是1個相等
            dp[2][0] = 1 => 雖然s[2]!=t[0]，但到目前為止 是1個相等
            dp[3][0] = 1 => 雖然s[3]!=t[0]，但到目前為止 是1個相等
            .
            .
            .
            所以dp[i][0] = 1 (i=0~m 都要=1) 
            ##############
            
        
        loop：
            s: xxxx i
            t: yyy j

            若s[i] != t[j] => s[:i-1]的情況下走到t[j]的相同個數 => dp[i][j] = dp[i-1][j]
            若s[i] == t[j] => 除了上面的之外，還要再考慮s[:i-1]走到t[:j-1]的相同個數 => dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        '''
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # init
        for i in range(m+1):
            dp[i][0] = 1
        
        # loop
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n]
