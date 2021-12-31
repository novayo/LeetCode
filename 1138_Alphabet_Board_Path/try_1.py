class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        table = {}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                table[board[i][j]] = (i, j)
        
        cur_word = 'a'
        movement = ''
        for t in target:
            move = ''
            if cur_word != t:
                move = self.move_posA_to_posB(table[cur_word], table[t])
                cur_word = t
            movement += move + '!'
        
        return movement
    
    def move_posA_to_posB(self, posA, posB):
        diff_x = posA[0] - posB[0]
        diff_y = posA[1] - posB[1]
        
        movement = ''
        end = ''
        if self.isZ(posA):
            movement += 'U'
            diff_x -= 1
        
        if self.isZ(posB):
            end = 'D'
            diff_x += 1
        
        movement += ('U' if diff_x > 0 else 'D') * abs(diff_x)
        movement += ('L' if diff_y > 0 else 'R') * abs(diff_y)
        
        return movement + end
    
    def isZ(self, pos):
        return pos[0] == 5 and pos[1] == 0
            
