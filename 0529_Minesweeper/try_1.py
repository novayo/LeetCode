class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        '''
        M -> X
        E -> B
        '''
        def calculate_mine(x, y):
            bombs = 0
            for i, j in [x-1,y-1], [x-1,y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1], [x, y-1]:
                if i < 0 or j < 0 or i >= height or j >= width:
                    continue
                if board[i][j] == 'M':
                    bombs += 1
            return bombs
        
        
        height = len(board)
        width = len(board[0])
        
        queue = set()
        queue.add((click[0], click[1]))

        while queue:
            x, y = queue.pop()
            
            if board[x][y] == 'M':
                board[x][y] = 'X'
                break
            
            board[x][y] = 'B'
            
            bombs = calculate_mine(x, y)
            if bombs > 0:
                board[x][y] = str(bombs)
            else:
                for i, j in [x-1,y-1], [x-1,y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1], [x, y-1]:
                    if i < 0 or j < 0 or i >= height or j >= width:
                        continue
                    if board[i][j] == 'E':
                        queue.add((i, j))
        
        return board
