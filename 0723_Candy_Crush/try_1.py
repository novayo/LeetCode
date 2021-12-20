class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        height = len(board)
        width = len(board[0])
        
        while True:
            self.scan_vertically(height, width, board)
            self.scan_horizontally(height, width, board)        

            if self.move(height, width, board):
                break
                
        return board
    
    def move(self, height, width, board):
        flag = True
        for j in range(width):
            count = 0
            k = 0
            for i in range(height-1, -1, -1):
                if board[i][j] < 0:
                    count += 1
                elif board[i][j] == 0:
                    k = i+1
                    break
                else:
                    board[i+count][j] = board[i][j]
            
            for i in range(k, k+count):
                flag = False
                board[i][j] = 0
        return flag
    
    def scan_horizontally(self, height, width, board):
        for i in range(height):
            s = e = width-1
            
            while s >= 0:
                while e >= 0 and (board[i][s] == board[i][e] or board[i][s] == -board[i][e]):
                    e -= 1
                
                if s-e >= 3:
                    while s > e:
                        if board[i][s] > 0: board[i][s] *= -1
                        s -= 1
                s = e
    
    def scan_vertically(self, height, width, board):
        for j in range(width):
            s = e = height-1
            
            while s >= 0:
                while e >= 0 and (board[s][j] == board[e][j] or board[s][j] == -board[e][j]):
                    e -= 1
                
                if s-e >= 3:
                    while s > e:
                        if board[s][j] > 0: board[s][j] *= -1
                        s -= 1
                s = e
            
            
