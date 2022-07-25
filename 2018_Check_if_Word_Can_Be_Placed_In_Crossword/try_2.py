class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # O(mn) time / O(1) space
        height, width = len(board), len(board[0])
        length = len(word)
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == '#':
                    continue
                
                # row
                if not j+length > width and (j == 0 or board[i][j-1] == '#') and (j+length == width or board[i][j+length] == '#'):
                    flag = True
                    for k in range(j, j+length):
                        if not (board[i][k] == ' ' or board[i][k] == word[k-j]):
                            flag = False
                            break
                    if flag:
                        return True
                    
                    flag = True
                    for k in range(j+length-1, j-1, -1):
                        if not (board[i][k] == ' ' or board[i][k] == word[j+length-1 - k]):
                            flag = False
                            break
                    if flag:
                        return True
                
                # col
                if not i+length > height and (i == 0 or board[i-1][j] == '#') and (i+length == height or board[i+length][j] == '#'):
                    flag = True
                    for k in range(i, i+length):
                        if not (board[k][j] == ' ' or board[k][j] == word[k-i]):
                            flag = False
                            break
                    if flag:
                        return True
                    
                    flag = True
                    for k in range(i+length-1, i-1, -1):
                        if not (board[k][j] == ' ' or board[k][j] == word[i+length-1 - k]):
                            flag = False
                            break
                    if flag:
                        return True
        return False
