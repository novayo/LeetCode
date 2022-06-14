class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        height = len(matrix)
        width = len(matrix[0])
        
        memo = {}
        def dfs(i, j):
            if (i, j) not in memo:
                ret = 0
                for _i, _j in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                    if _i < 0 or _j < 0 or _i >= height or _j >= width:
                        continue

                    if matrix[_i][_j] <= matrix[i][j]:
                        continue

                    ret = max(ret, dfs(_i, _j))
                memo[i, j] = ret + 1
            return memo[i, j]
        
        ans = 0
        for i in range(height):
            for j in range(width):
                ans = max(ans, dfs(i, j))
        return ans
        