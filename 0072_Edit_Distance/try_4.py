class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # dp[i][j] = word1[i:] == word2[j:] 的次數
        
        # init
        for idx1 in range(m-1, -1, -1):
            dp[idx1][n] = m - idx1
            
        for idx2 in range(n, -1, -1):
            dp[m][idx2] = n - idx2
        
        # dp
        for idx1 in range(m-1, -1, -1):
            for idx2 in range(n-1, -1, -1):
                if word1[idx1] == word2[idx2]:
                    dp[idx1][idx2] = dp[idx1+1][idx2+1]
                else:                
                    dp[idx1][idx2] = 1 + min(
                        dp[idx1+1][idx2+1],
                        dp[idx1+1][idx2],
                        dp[idx1][idx2+1]
                    )
        
        return dp[0][0]
