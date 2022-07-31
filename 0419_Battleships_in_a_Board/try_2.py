class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def mark(i, j):
            board[i][j] = '.'
            for k in range(j+1, width):
                if board[i][k] == 'X':
                    board[i][k] = '.'
                else:
                    break
            for k in range(i+1, height):
                if board[k][j] == 'X':
                    board[k][j] = '.'
                else:
                    break
        
        height, width = len(board), len(board[0])
        ret = 0
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'X':
                    ret += 1
                    mark(i, j)
        return ret
