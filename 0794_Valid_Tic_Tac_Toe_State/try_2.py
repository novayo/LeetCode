class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        '''
        X的數量 >= O + 1的數量
        不能同時兩個人贏
        if X贏了 => X的數量一定 > O的數量
        if O贏了 => X的數量一定 = O的數量
        '''
        rows = [collections.Counter() for _ in range(3)]
        cols = [collections.Counter() for _ in range(3)]
        diag = collections.Counter()
        anti_diag = collections.Counter()
        numbers = collections.Counter()
        wins = set()
        
        for i in range(3):
            for j in range(3):
                for player in 'XO':
                    if board[i][j] == player:
                        numbers[player] += 1
                        rows[i][player] += 1
                        if rows[i][player] >= 3:
                            wins.add(player)
                        
                        cols[j][player] += 1
                        if cols[j][player] >= 3:
                            wins.add(player)
                        
                        if i - j == 0:
                            diag[player] += 1
                            if diag[player] >= 3:
                                wins.add(player)
                        
                        if i + j == 2:
                            anti_diag[player] += 1
                            if anti_diag[player] >= 3:
                                wins.add(player)
        
        if not (numbers['O'] <= numbers['X'] <= numbers['O'] + 1):
            return False
        
        if len(wins) == 2:
            return False
        
        if len(wins) == 1:
            winner = list(wins)[0]
            if winner == 'X':
                if not (numbers['X'] > numbers['O']):
                    return False
            else:
                if not (numbers['X'] == numbers['O']):
                    return False
        return True
        
