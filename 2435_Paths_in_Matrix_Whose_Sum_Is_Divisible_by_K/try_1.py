class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        MOD = k
        M = 10 ** 9 + 7
        
        dp = [[collections.Counter() for _ in range(n)] for _ in range(m)]
        
        dp[0][0][grid[0][0] % MOD] = 1
        for i in range(1, m):
            val = grid[i][0]
            for k, v in dp[i - 1][0].items():
                dp[i][0][(k + val) % MOD] += v % M
                
        for j in range(1, n):
            val = grid[0][j]
            for k, v in dp[0][j - 1].items():
                dp[0][j][(k + val) % MOD] += v % M
                
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                for k, v in dp[i][j - 1].items():
                    dp[i][j][(k + val) % MOD] += v % M
        
                for k, v in dp[i - 1][j].items():
                    dp[i][j][(k + val) % MOD] += v % M     
                    
        return dp[-1][-1][0] % M