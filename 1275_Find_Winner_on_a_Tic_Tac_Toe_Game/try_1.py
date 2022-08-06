class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [collections.Counter() for _ in range(3)]
        cols = [collections.Counter() for _ in range(3)]
        diag = collections.Counter()
        anti_diag = collections.Counter()
        
        
        player = 'A'
        for i, j in moves:
            rows[i][player] += 1
            if rows[i][player] >= 3:
                return player
            
            cols[j][player] += 1
            if cols[j][player] >= 3:
                return player
            
            if i - j == 0:
                diag[player] += 1
                if diag[player] >= 3:
                    return player
                
            if i + j == 2:
                anti_diag[player] += 1
                if anti_diag[player] >= 3:
                    return player
            
            if player == 'A':
                player = 'B'
            else:
                player = 'A'
            
        return 'Draw' if len(moves) == 9 else 'Pending'
