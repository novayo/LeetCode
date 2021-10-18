class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        for layer in range(height-2, -1, -1):
            
            for i in range(width):
                left = matrix[layer+1][i-1] if i > 0 else float('inf')
                mid = matrix[layer+1][i]
                right = matrix[layer+1][i+1] if i < width-1 else float('inf')
                
                matrix[layer][i] += min(left, mid, right)
        
        return min(matrix[0])