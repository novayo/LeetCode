class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def recr(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'
            recr(i-1, j)
            recr(i, j-1)
            recr(i+1, j)
            recr(i, j+1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    recr(i, j)
                    ans += 1
        return ans
