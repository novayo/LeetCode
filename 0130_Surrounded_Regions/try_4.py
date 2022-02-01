class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def flip(i, j, sign):
            if i < 0 or j < 0 or i >= height or j >= width or board[i][j] == 'X' or board[i][j] == sign:
                return
            
            board[i][j] = sign
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                flip(x, y, sign)
        
        
        height = len(board)
        width = len(board[0])
        
        # flip arround to 'W' => wait to flip back
        for i in range(height):
            if board[i][0] == 'O':
                flip(i, 0, 'W')
            if board[i][width-1] == 'O':
                flip(i, width-1, 'W')
        for j in range(width):
            if board[0][j] == 'O':
                flip(0, j, 'W')
            if board[height-1][j] == 'O':
                flip(height-1, j, 'W')
        
        # flip remain 'O' to 'X'
        for i in range(1, height-1):
            for j in range(1, width-1):
                if board[i][j] == 'O':
                    flip(i, j, 'X')
        
        # flip 'W' to 'O'
        for i in range(height):
            if board[i][0] == 'W':
                flip(i, 0, 'O')
            if board[i][width-1] == 'W':
                flip(i, width-1, 'O')
        for j in range(width):
            if board[0][j] == 'W':
                flip(0, j, 'O')
            if board[height-1][j] == 'W':
                flip(height-1, j, 'O')
        
