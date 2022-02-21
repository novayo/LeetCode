class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        height = len(board)
        width = len(board[0])
        
        def backtracking(i, j, index):
            nonlocal memo
            
            if index >= n:
                return True
            
            memo.add((i, j))
            
            for x, y in [i, j+1], [i, j-1], [i+1, j], [i-1, j]:
                if x < 0 or y < 0 or x >= height or y >= width or (x, y) in memo:
                    continue
                
                if board[x][y] == word[index]:
                    if backtracking(x, y, index+1):
                        return True
            
            memo.remove((i, j))
            
            return False
        
        
        for i in range(height):
            for j in range(width):
                memo = set()
                if board[i][j] == word[0]:
                    if backtracking(i, j, 1):
                        return True
        return False
        