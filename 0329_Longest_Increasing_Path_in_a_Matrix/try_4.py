class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(matrix), len(matrix[0])
        
        memo = {}
        def recr(i, j):
            if (i, j) in memo:
                return memo[i, j]
            
            ret = 0
            for x, y in [i+1,j], [i,j+1], [i-1,j], [i,j-1]:
                if not (0 <= x < HEIGHT and 0 <= y < WIDTH):
                    continue
                
                if matrix[x][y] > matrix[i][j]:
                    ret = max(ret, recr(x, y))
            
            memo[i, j] = ret + 1
            return memo[i, j]
        
        
        ans = 0
        for i in range(HEIGHT):
            for j in range(WIDTH):
                ans = max(ans, recr(i, j))
        return ans

