class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cols = len(grid)
        rows = len(grid[0])
        
        for col in range(cols):
            for row in range(rows):
                up = float('inf') if col == 0 else grid[col-1][row]
                left = float('inf') if row == 0 else grid[col][row-1]
                
                if up == left == float('inf'):
                    continue
                grid[col][row] += min(up, left)
        
        return grid[cols-1][rows-1]
