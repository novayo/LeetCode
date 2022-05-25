class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        '''
        橫/直 => 查看第一個即可
        '''
        height = len(board)
        width = len(board[0])
        L = len(word)
        
        # check horizontally
        for i in range(height):
            j = 0
            while j+L <= width:
                if board[i][j] != '#':
                    if j+L == width or board[i][j+L] == '#':
                        if all([board[i][j+k] == ' ' or word[k] == board[i][j+k] for k in range(L)]):
                            return True
                        if all([board[i][j+k] == ' ' or word[~k] == board[i][j+k] for k in range(L)]):
                            return True
                    
                    j += 1
                    while j < width and board[i][j] != '#':
                        j += 1
                j += 1
        
        # check vertically
        for j in range(width):
            i = 0
            while i+L <= height:
                if board[i][j] != '#':
                    if i+L == height or board[i+L][j] == '#':
                        if all([board[i+k][j] == ' ' or word[k] == board[i+k][j] for k in range(L)]):
                            return True
                        if all([board[i+k][j] == ' ' or word[~k] == board[i+k][j] for k in range(L)]):
                            return True
                    
                    i += 1
                    while i < height and board[i][j] != '#':
                        i += 1
                i += 1
        
        return False