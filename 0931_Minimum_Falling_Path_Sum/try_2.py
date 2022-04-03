class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def get(i, j):
            if not (0 <= i < height) or not (0 <= j < width):
                return float('inf')
            return matrix[i][j]
        
        height = len(matrix)
        width = len(matrix[0])
        
        for i in range(height-2, -1, -1):
            for j in range(width):
                matrix[i][j] += min(
                    get(i+1, j-1),
                    get(i+1, j),
                    get(i+1, j+1)
                )
        return min(matrix[0])
