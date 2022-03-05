class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        '''
        1 >= num_x - num_o >= 0
        only one player wins
        '''
        # check num
        counter = collections.Counter()
        for i in range(3):
            for j in range(3):
                counter[board[i][j]] += 1
        
        if not(1 >= counter['X'] - counter['O'] >= 0):
            return False
        
        
        # check winers
        winners = []
        
        for p in range(2):
            target = 'X' if p == 0 else 'O'
            rows = [0] * 3
            cols = [0] * 3
            diganal = anti_diganal = 0
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] == target:
                        rows[i] += 1
                        cols[j] += 1
                        if i-j == 0: diganal += 1
                        if i+j == 2: anti_diganal += 1
                            
                        if rows[i] >= 3 or cols[j] >= 3 or diganal >= 3 or anti_diganal >= 3:
                            winners.append(target)
                            break
                if len(winners) > p:
                    break
        
        if len(winners) == 1:
            if winners[0] == 'O' and counter['X'] > counter['O']:
                return False
            elif winners[0] == 'X' and counter['X'] <= counter['O']:
                return False
        return len(winners) < 2

