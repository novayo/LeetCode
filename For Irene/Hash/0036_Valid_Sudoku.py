class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        
        rows = [set() for i in range(length)]   # x 
        cols = [set() for i in range(length)]   # y
        blocks = [set() for i in range(length)] # x // 3 * 3 + y // 3 => block index
        
        # O(m*n)
        for x in range(length):
            for y in range(length):
                if board[x][y] == '.':
                    continue
                
                index_blocks = x // 3 * 3 + y // 3
                if board[x][y] in rows[x] or board[x][y] in cols[y] or board[x][y] in blocks[index_blocks]:
                    return False

                rows[x].add(board[x][y])
                cols[y].add(board[x][y])
                blocks[index_blocks].add(board[x][y])
        
        return True