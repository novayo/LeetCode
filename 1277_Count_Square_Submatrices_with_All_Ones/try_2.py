class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        12
        2min(left, up, left_up) + 1 => add to ans
        '''
        height, width = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(height):
            for j in range(width):
                if matrix[i][j] != 1:
                    continue
                
                left = matrix[i][j-1] if j > 0 else 0
                up = matrix[i-1][j] if i > 0 else 0
                left_up = matrix[i-1][j-1] if i>0 and j>0 else 0
                
                matrix[i][j] = min(left, up, left_up) + 1
                ans += matrix[i][j]
                
        return ans
