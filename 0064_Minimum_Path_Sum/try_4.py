class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        height = len(grid)
        width = len(grid[0])
        
        for i in range(1, height):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, width):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, height):
            for j in range(1, width):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[height-1][width-1]
