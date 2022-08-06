class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        rows = [collections.Counter() for _ in range(3)]
        cols = [collections.Counter() for _ in range(3)]
        diag = collections.Counter()
        anti_diag = collections.Counter()
        number_of_X = number_of_O = 0
        win = set()
        
        for i in range(3):
            for j in range(3):
                symbol = ''
                if board[i][j] == 'X':
                    number_of_X += 1
                    symbol = 'X'
                elif board[i][j] == 'O':
                    number_of_O += 1
                    symbol = 'O'
                else:
                    continue
                    
                rows[i][symbol] += 1
                cols[j][symbol] += 1
                
                if rows[i][symbol] >= 3:
                    win.add(symbol)
                if cols[j][symbol] >= 3:
                    win.add(symbol)

                if i-j == 0:
                    diag[symbol] += 1
                    if diag[symbol] >= 3:
                        win.add(symbol)
                if i+j == 2:
                    anti_diag[symbol] += 1
                    if anti_diag[symbol] >= 3:
                        win.add(symbol)
        
        if not (0 <= number_of_X - number_of_O <= 1):
            return False
        
        if len(win) == 2:
            return False
        
        if ('X' in win and number_of_X == number_of_O) or ('O' in win and number_of_X > number_of_O):
            return False
        
        return True