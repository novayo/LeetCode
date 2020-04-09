class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for col in range(m):
            for row in range(n):
                if col > 0:
                    dp[col][row] += dp[col-1][row]
                if row > 0:
                    dp[col][row] += dp[col][row-1]
        return dp[m-1][n-1]
