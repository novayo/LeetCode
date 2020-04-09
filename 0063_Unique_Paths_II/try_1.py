class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        cols = len(obstacleGrid)
        rows = len(obstacleGrid[0])
        
        dp = [[0]*rows for _ in range(cols)]
        dp[0][0] = 1
        
        for col in range(cols):
            for row in range(rows):
                if obstacleGrid[col][row] == 1:
                    dp[col][row] = 0
                else:
                    if col > 0:
                        dp[col][row] += dp[col-1][row]
                    if row > 0:
                        dp[col][row] += dp[col][row-1]
        return dp[cols-1][rows-1]
