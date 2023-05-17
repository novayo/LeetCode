class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # init data
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[i//3*3 + j//3].add(board[i][j])

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
                    s = f"{v}"
                    if s in rows[i] or s in cols[j] or s in boxes[i//3*3 + j//3]:
                        continue
                    
                    rows[i].add(s)
                    cols[j].add(s)
                    boxes[i//3*3 + j//3].add(s)
                    board[i][j] = s
                    
                    if recr(i, j+1):
                        return True
                    
                    rows[i].remove(s)
                    cols[j].remove(s)
                    boxes[i//3*3 + j//3].remove(s)
                    board[i][j] = '.'
            
            return False
        
        recr(0, 0)

