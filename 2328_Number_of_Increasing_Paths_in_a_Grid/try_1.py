class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        height, width = len(grid), len(grid[0])
        
        @functools.lru_cache(None)
        def recr(i, j):
            _sum = 1
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width) or grid[i][j] >= grid[x][y]:
                    continue
                _sum += recr(x, y)
            return _sum
        
        ans = 0
        for i in range(height):
            for j in range(width):
                ans = (ans + recr(i, j)) % MOD
        return ans