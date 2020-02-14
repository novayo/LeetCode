class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = collections.deque()
        
        def dfs(queens, Slope_1, Slope_neg_1):
            x = len(queens)
            if x == n:
                ans.append(queens)
                return
            for y in range(n):
                if y not in queens and x - y not in Slope_1 and x + y not in Slope_neg_1:
                    dfs(queens + [y], Slope_1 + [x-y], Slope_neg_1 + [x+y])
            
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n-i-1) for i in sol] for sol in ans]
