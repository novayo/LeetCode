class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i//3*3 + j//3].add(board[i][j])
        
        def recr(i, j):
            if j >= 9:
                i += 1
                j = 0
            
            if i >= 9:
                return True
            
            if board[i][j] != '.':
                if recr(i, j+1):
                    return True
            else:
                for v in range(1, 9+1):
                    v = f"{v}"
                    if v not in rows[i] and v not in cols[j] and v not in squares[i//3*3 + j//3]:
                        rows[i].add(v)
                        cols[j].add(v)
                        squares[i//3*3 + j//3].add(v)
                        board[i][j] = v
                        
                        if recr(i, j+1):
                            return True
                        
                        board[i][j] = '.'
                        rows[i].remove(v)
                        cols[j].remove(v)
                        squares[i//3*3 + j//3].remove(v)
            
            return False
        
        recr(0, 0)
        return board
