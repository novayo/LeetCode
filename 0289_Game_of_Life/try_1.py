class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        此點 = 1 => 周圍 <= 1   => 此點 = 0
        此點 = 1 => 周圍 == 2 3 => 此點 = 1
        此點 = 1 => 周圍 > 3    => 此點 = 0
        此點 = 0 => 周圍 == 3   => 此點 = 1
        
        原本 = 0, 新的 = 0 => 0
        原本 = 0, 新的 = 1 => -1
        原本 = 1, 新的 = 0 => -2
        原本 = 1, 新的 = 1 => 1
        '''
        ORIGINAL_ZERO = -1
        ORIGINAL_ONE  = -2
        
        height = len(board)
        width = len(board[0])
        
        for i in range(height):
            for j in range(width):
                # count neighbors
                neighbors = 0
                for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1], [i+1, j+1], [i+1, j-1], [i-1, j+1], [i-1, j-1]:
                    if x < 0 or y < 0 or x >= height or y >= width or board[x][y] in [0, ORIGINAL_ZERO]:
                        continue
                    neighbors += 1
                    
                if board[i][j] == 0:
                    if neighbors == 3:
                        board[i][j] = ORIGINAL_ZERO
                else:
                    if neighbors <= 1 or neighbors > 3:
                        board[i][j] = ORIGINAL_ONE
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == ORIGINAL_ZERO:
                    board[i][j] = 1
                elif board[i][j] == ORIGINAL_ONE:
                    board[i][j] = 0
                    
                