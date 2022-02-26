class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''
        k = 0 => 1*1
        k = 1 => 3*3
        k = 2 => 5*5
        
        presum
        '''
        def get(i, j):
            if i < 0 or j < 0 or i >= height or j >= width:
                return 0
            return mat[i][j]
        
        height = len(mat)
        width = len(mat[0])
        
        # presum
        dp = [[0] * width for _ in range(height)]
        for j in range(width):
            for i in range(k+1):
                for _j in range(j-k, j+k+1):
                    dp[0][j] += get(i, _j)
        
        # move down
        for i in range(1, height):
            # update every value by row
            for j in range(width):
                dp[i][j] = dp[i-1][j]
                # minus top, add down
                top, down = i-k-1, i+k
                for _j in range(j-k, j+k+1):
                    dp[i][j] = dp[i][j] - get(top, _j) + get(down, _j)
        
        return dp
