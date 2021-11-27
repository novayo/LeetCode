class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rowTable = {}
        colTable = {}
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    if i not in rowTable:
                        self.countRow(grid, rowTable, i, j)
                    if j not in colTable:
                        self.countCol(grid, colTable, i, j)
                    
                    row_enemy = rowTable[i]
                    col_enemy = colTable[j]
                    
                    ans = max(ans, row_enemy + col_enemy)
                elif grid[i][j] == 'W':
                    if i in rowTable:
                        del rowTable[i]
                    if j in colTable:
                        del colTable[j]
        
        return ans
        
        
    def countRow(self, grid, rowTable, i, j):
        l, r = j-1, j+1

        count = 0
        while l >= 0:
            if grid[i][l] == 'W':
                break

            if grid[i][l] == 'E':
                count += 1
            l -= 1

        while r < len(grid[i]):
            if grid[i][r] == 'W':
                break

            if grid[i][r] == 'E':
                count += 1
            r += 1

        rowTable[i] = count
        
    def countCol(self, grid, colTable, i, j):
        u, d = i-1, i+1

        count = 0
        while u >= 0:
            if grid[u][j] == 'W':
                break
            if grid[u][j] == 'E':
                count += 1
            u -= 1

        while d < len(grid):
            if grid[d][j] == 'W':
                break
            if grid[d][j] == 'E':
                count += 1
            d += 1
            
        colTable[j] = count
