class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        def recr(i, j, steps):
            nonlocal memo
            if i < 0 or j < 0 or i >= n or j >= n:
                return 0
            if steps <= 0:
                return 1
            
            if (i, j, steps) in memo:
                return memo[i, j, steps]
            
            ret = 0
            for x, y in [i-2, j+1], [i-1, j+2], [i+1, j+2], [i+2, j+1], [i+2, j-1], [i+1, j-2], [i-1, j-2], [i-2, j-1]:
                ret += recr(x, y, steps-1)
            
            memo[i, j, steps] = ret
            return memo[i, j, steps]
        
        return recr(row, column, k) / (8**k)
