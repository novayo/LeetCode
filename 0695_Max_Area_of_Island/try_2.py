class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        def dfs(i, j, container):
            if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            container[0] += 1
            
            for x, y in [i, j-1], [i, j+1], [i-1, j], [i+1, j]:
                dfs(x, y, container)
        
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    cur_ans = [0]
                    dfs(i, j, cur_ans)
                    ans = max(ans, cur_ans[0])
        return ans
