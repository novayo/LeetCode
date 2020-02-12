class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        # 暴力
        def recr(puzzle, x, y):
            nonlocal ans
            if y >= n:
                y -= n
            # print(puzzle, x, y)
            if x >= n:
                ans.append(self.joinMap(puzzle))
                return True
            if self.if_feasible(puzzle, x, y):
                puzzle[x][y] = "Q"
                for i in range(n):
                    if recr(puzzle, x+1, y+i):
                        break
                puzzle[x][y] = "."
            else:
                return
            
        puzzle = [["."]*n for i in range(n)]
        ans = collections.deque()
        for i in range(n):
            recr(puzzle, 0, i)
        return ans
    
    def if_feasible(self, puzzle, x, y) -> bool:
        righty = lefty = y
        while x > 0:
            x -= 1
            
            # 上
            if puzzle[x][y] == 'Q':
                return False
            
            # 左斜
            if lefty > 0:
                lefty -= 1
                if puzzle[x][lefty] == 'Q':
                    return False
                
            # 右斜
            if righty < len(puzzle) - 1:
                righty += 1
                if puzzle[x][righty] == 'Q':
                    return False
        return True
    
    def joinMap(self, puzzle):
        return [''.join(puzzle[i]) for i in range(len(puzzle))]
