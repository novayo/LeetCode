class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # init
        ans = 0
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            ans = max(matrix[i][0], ans)
        
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            ans = max(matrix[0][j], ans)
        
        # get ans
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    matrix[i][j] = min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    ) + 1
                    ans = max(ans, matrix[i][j])
        
        return pow(ans, 2)
        
