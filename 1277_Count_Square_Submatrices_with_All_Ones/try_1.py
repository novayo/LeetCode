class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        compute max square => sum is the answer
        '''
        height = len(matrix)
        width = len(matrix[0])
        ans = 0
        
        # init
        for i in range(height):
            if matrix[i][0] == 1:
                ans += 1
        for j in range(1, width):
            if matrix[0][j] == 1:
                ans += 1
        
        # loop
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] == 0:
                    continue
                
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                ans += matrix[i][j]
        
        return ans
                