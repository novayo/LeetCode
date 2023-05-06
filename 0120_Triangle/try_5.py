class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        
        memo = {}
        def recr(i, j):
            if i >= ROWS:
                memo[i, j] = 0
                return 0
            
            if (i, j) in memo:
                return memo[i, j]
            
            memo[i, j] = triangle[i][j] + min(recr(i+1, j), recr(i+1, j+1))
            return memo[i, j]
        
        return recr(0, 0)
