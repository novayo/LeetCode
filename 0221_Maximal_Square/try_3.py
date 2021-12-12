class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        2 1
        2 [3]
        '''
        height = len(matrix)
        width = len(matrix[0])
        ans = 0
        
        # init
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    ans = 1
                    break
        
        # loop
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] == '0':
                    continue
                _min = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1]))
                
                if _min > 0:
                    matrix[i][j] = str(_min + 1)
                    ans = max(ans, _min+1)

        return ans*ans
