class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        先+4，上下左右有的-1
        '''
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 4 - (i + 1 < row and grid[i + 1][j]) - (i - 1 >= 0 and grid[i - 1][j]) \
                             - (j + 1 < col and grid[i][j + 1]) - (j - 1 >= 0 and grid[i][j - 1])
        return ans