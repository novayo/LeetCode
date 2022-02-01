class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        dp = [[0] * width for _ in range(height)]
        
        # init
        for j in range(width):
            obs = obstacleGrid[0][j]
            if obs == 0:
                dp[0][j] = 1
            else:
                break
        
        for i in range(height):
            obs = obstacleGrid[i][0]
            if obs == 0:
                dp[i][0] = 1
            else:
                break
        
        # loop
        for i in range(1, height):
            for j in range(1, width):
                obs = obstacleGrid[i][j]
                
                if obs == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[height-1][width-1]
