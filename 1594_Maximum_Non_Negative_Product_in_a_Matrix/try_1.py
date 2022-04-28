class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        height = len(grid)
        width = len(grid[0])
        
        dp = [[[-1, -1] for _ in range(width)] for __ in range(height)]
        dp[0][0] = [grid[0][0], grid[0][0]]
        
        # grid[0][*]
        for j in range(1, width):
            all_possible = [
                grid[0][j] * dp[0][j-1][0],
                grid[0][j] * dp[0][j-1][1]
            ]
            dp[0][j] = [min(all_possible), max(all_possible)]
        
        # grid[*][0]
        for i in range(1, height):
            all_possible = [
                grid[i][0] * dp[i-1][0][0],
                grid[i][0] * dp[i-1][0][1]
            ]
            dp[i][0] = [min(all_possible), max(all_possible)]
        
        # grid[*][*]
        for i in range(1, height):
            for j in range(1, width):
                all_possible = [
                    grid[i][j] * dp[i-1][j][0], 
                    grid[i][j] * dp[i-1][j][1],
                    grid[i][j] * dp[i][j-1][0],
                    grid[i][j] * dp[i][j-1][1]
                ]
                dp[i][j] = [min(all_possible), max(all_possible)]
        
        return dp[-1][-1][1] % MOD if dp[-1][-1][1] >= 0 else -1