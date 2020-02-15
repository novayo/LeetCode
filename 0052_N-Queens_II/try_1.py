class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        
        def dfs(queens, Slope_1, Slope_neg_1):
            x = len(queens)
            if x == n:
                self.ans += 1
                return
            for y in range(n):
                if y not in queens and x - y not in Slope_1 and x + y not in Slope_neg_1:
                    dfs(queens + [y], Slope_1 + [x-y], Slope_neg_1 + [x+y])
            
        dfs([], [], [])
        return self.ans
