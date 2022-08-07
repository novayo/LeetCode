class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        n = len(word)
        
        for i in range(height):
            for j in range(width):
                
                # check up
                if (i-n >= -1) and (i == height-1 or board[i+1][j] == '#') and (i-n == -1 or board[i-n][j] == '#'):
                    isAnswer = True
                    for k in range(n):
                        if not (board[i-k][j] == ' ' or board[i-k][j] == word[k]):
                            isAnswer = False
                            break
                    if isAnswer:
                        return True
                
                # check right
                if (j+n <= width) and (j == 0 or board[i][j-1] == '#') and (j+n == width or board[i][j+n] == '#'):
                    isAnswer = True
                    for k in range(n):
                        if not (board[i][j+k] == ' ' or board[i][j+k] == word[k]):
                            isAnswer = False
                            break
                    if isAnswer:
                        return True
                
                # check down
                if (i+n <= height) and (i == 0 or board[i-1][j] == '#') and (i+n == height or board[i+n][j] == '#'):
                    isAnswer = True
                    for k in range(n):
                        if not (board[i+k][j] == ' ' or board[i+k][j] == word[k]):
                            isAnswer = False
                            break
                    if isAnswer:
                        return True
                
                # check left
                if (j-n >= -1) and (j == width-1 or board[i][j+1] == '#') and (j-n == -1 or board[i][j-n] == '#'):
                    isAnswer = True
                    for k in range(n):
                        if not (board[i][j-k] == ' ' or board[i][j-k] == word[k]):
                            isAnswer = False
                            break
                    if isAnswer:
                        return True
        return False
