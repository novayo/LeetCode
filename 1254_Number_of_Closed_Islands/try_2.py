class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] != 0:
                return
            
            grid[i][j] = 1
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        ans = 0
        for i in range(height):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][width-1] == 0:
                dfs(i, width-1)
        for j in range(width):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[height-1][j] == 0:
                dfs(height-1, j)
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        
        return ans
