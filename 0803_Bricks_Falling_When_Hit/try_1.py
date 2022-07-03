class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = MARKED # mark stable
            ret = 1
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                ret += dfs(x, y)
            return ret
        
        def isStable(i, j):
            return i == 0 or any([0<=x<m and 0<=y<n and grid[x][y]==MARKED for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])
        
        MARKED = 100
        m, n, k = len(grid), len(grid[0]), len(hits)
        
        # hits all
        for i, j in hits:
            grid[i][j] -= 1
        
        # mark stable from top
        for j in range(n):
            dfs(0, j)
        
        # reverse back
        ans = [0] * k
        for _k in range(k-1, -1, -1):
            i, j = hits[_k]
            grid[i][j] += 1
            
            if grid[i][j] == 1 and isStable(i, j):
                ans[_k] += dfs(i, j) - 1
        return ans
            
            