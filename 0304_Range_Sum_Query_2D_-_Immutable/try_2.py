class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
        self.dp[1][1] = matrix[0][0]
        for i in range(2, len(matrix)+1):
            self.dp[i][1] += self.dp[i-1][1] + matrix[i-1][0]
        for j in range(2, len(matrix[0])+1):
            self.dp[1][j] += self.dp[1][j-1] + matrix[0][j-1]
        
        for i in range(2, len(matrix)+1):
            for j in range(2, len(matrix[0])+1):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_down = (row2+1, col1+1-1)
        right_top = (row1+1-1, col2+1)
        left_top = (row1+1-1, col1+1-1)
        right_down = (row2+1, col2+1)
        
        return self.dp[right_down[0]][right_down[1]] - \
               self.dp[right_top[0]][right_top[1]] - \
               self.dp[left_down[0]][left_down[1]] + \
               self.dp[left_top[0]][left_top[1]] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
