class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        上左是石頭的則+0
        '''
        dp = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        
        # 1th row
        flag = True
        for j in range(len(obstacleGrid[0])):
            if flag and obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
                flag = False
        
        # 1th col
        flag = True
        for i in range(len(obstacleGrid)):
            if flag and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                flag = False
        
        # loop remain
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]