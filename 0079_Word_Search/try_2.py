class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index=1, memo=set()):
            if index >= len(word):
                return True
            
            memo.add((i, j))
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if x < 0 or y < 0 or x>=m or y>=n or (x, y) in memo or board[x][y] != word[index]:
                    continue
                if dfs(x, y, index+1):
                    return True
            
            memo.remove((i, j))
            
            return False
                    
        
        m = len(board)
        n = len(board[0])
        length = len(word)
        
        # init
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j):
                        return True
        return False
