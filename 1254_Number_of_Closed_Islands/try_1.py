class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        def dfs(i, j, ret):
            if grid[i][j] == 1:
                return
            
            if i <= 0 or i >= height-1 or j <= 0 or j >= width-1:
                ret[0] = False
                return
            
            grid[i][j] = 1
            
            dfs(i-1, j, ret)
            dfs(i+1, j, ret)
            dfs(i, j-1, ret)
            dfs(i, j+1, ret)
        
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    callback = [True]
                    dfs(i, j, callback)
                    
                    if callback[0] == True:
                        ans += 1
        return ans