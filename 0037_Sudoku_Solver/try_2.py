class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        to_solve = collections.deque()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    cols[j].add(int(board[i][j]))
                    rows[i].add(int(board[i][j]))
                    blocks[i//3*3 + j//3].add(int(board[i][j]))
                else:
                    to_solve.append((i, j))
        
        def backtrack(board, i, j):
            if not to_solve:
                return True
            
            i, j = to_solve.pop()
            for k in range(1, 10):
                if k in rows[i] or k in cols[j] or k in blocks[i//3*3 + j//3]:
                    continue

                cols[j].add(k)
                rows[i].add(k)
                blocks[i//3*3 + j//3].add(k)
                board[i][j] = str(k)
                if backtrack(board, i, j+1):
                    return True
                cols[j].remove(k)
                rows[i].remove(k)
                blocks[i//3*3 + j//3].remove(k)
                board[i][j] = "."
            
            to_solve.append((i, j))
        
        backtrack(board, 0, 0)
