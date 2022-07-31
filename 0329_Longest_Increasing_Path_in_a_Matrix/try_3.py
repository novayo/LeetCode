class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            ret = 0
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width) or matrix[i][j] >= matrix[x][y]:
                    continue
                
                ret = max(ret, dfs(x, y))
            return ret + 1
        
        height, width = len(matrix), len(matrix[0])
        return max(dfs(i, j) for i in range(height) for j in range(width))