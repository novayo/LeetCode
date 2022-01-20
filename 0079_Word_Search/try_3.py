class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        height = len(board)
        width = len(board[0])
        
        def dfs(i, j, index, found):
            if index >= len(word):
                return True
            
            for x, y in [i+1, j], [i-1, j], [i, j-1], [i, j+1]:
                if x < 0 or x >= height or y < 0 or y >= width or (x, y) in found or board[x][y] != word[index]:
                    continue

                found.add((x, y))
                if dfs(x, y, index+1, found):
                    return True
                found.remove((x, y))
                
            return False
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, set([(i, j)])):
                        return True
        return False
