class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = []
        cols = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(len(board)):
            rows.append(set(board[i]))  
            for j in range(len(board[i])):
                cols[j].add(board[i][j])
                square[i//3][j//3].add(board[i][j])

        flag = False
        def dfs(i, j):
            nonlocal flag
            
            if flag:
                return
            
            if i >= len(board):
                flag = True
                return
            
            if board[i][j] != '.':
                if j+1 < len(board[0]):
                    dfs(i, j+1)
                else:
                    dfs(i+1, 0)
            else:
                for v in range(1, 10):
                    v = str(v)
                    if v in rows[i] or v in cols[j] or v in square[i//3][j//3]:
                        continue
                    
                    rows[i].add(v)
                    cols[j].add(v)
                    square[i//3][j//3].add(v)
                    board[i][j] = v
                    
                    if j+1 < len(board[0]):
                        dfs(i, j+1)
                    else:
                        dfs(i+1, 0)
                    if flag:
                        return
                    board[i][j] = '.'
                    rows[i].remove(v)
                    cols[j].remove(v)
                    square[i//3][j//3].remove(v)
        dfs(0,0)
