class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        '''
        如果不是從z出發，則要先走橫軸 => Ex: e~z
        如果從z出發，則要先走縱軸 => Ex: z~e
        '''
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        # build index
        index = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                index[board[i][j]] = (i, j)
        
        # get answer
        ans = ''
        current = 'a'
        
        for next in target:
            x, y = index[current]
            n_x, n_y = index[next]
            
            row_string = col_string = ''
            
            if x > n_x:
                col_string += 'U' * (x-n_x)
            else:
                col_string += 'D' * (n_x-x)
            
            if y > n_y:
                row_string += 'L' * (y-n_y)
            else:
                row_string += 'R' * (n_y-y)
            
            if current == 'z':
                ans += col_string + row_string
            else:
                ans += row_string + col_string
            
            ans += '!'
            current = next
        
        return ans
