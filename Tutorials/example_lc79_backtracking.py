class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(i, j, idx, cache):
            if idx == len(word)-1:
                return True
            
            for x, y in [i+1,j], [i-1,j], [i,j-1], [i,j+1]:
                if not (0 <= x < height and 0 <= y < width):
                    continue
                
                if (x, y) in cache or board[x][y] != word[idx+1]:
                    continue
                
                cache.add((i, j))
                if backtracking(x, y, idx+1, cache):
                    return True
                cache.remove((i, j))
            
            return False
        
        height, width = len(board), len(board[0])
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 0, set()):
                        return True
        return False
