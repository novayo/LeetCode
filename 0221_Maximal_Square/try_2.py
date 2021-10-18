class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        3*3 要保證 上的2*2 & 左的2*2 & 左上的2*2 皆為正方形 & 本身是1 => 才會是3*3
        
        但有可能 左上是4*4，此點是3*3 => 因此三方向要挑最小的出來+1
        '''
        ans = 0
        
        for i in range(len(matrix)):
            matrix[i][0] = int(matrix[i][0])
            ans = max(ans, matrix[i][0])
        
        for j in range(len(matrix[0])):
            matrix[0][j] = int(matrix[0][j])
            ans = max(ans, matrix[0][j])
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    ans = max(ans, matrix[i][j])
                else:
                    matrix[i][j] = int(matrix[i][j])
        
        return ans ** 2