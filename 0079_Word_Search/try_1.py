class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # using bfs
        # can't move to the arrived one
        def bfs(i, j, index, prestep):
            nonlocal ans
            if (ans): return
            tmp = board[i][j]
            board[i][j] = False
            if index == len(word):
                ans = True
                return
            if prestep != 2:
                if i - 1 >= 0:
                    if board[i-1][j] == word[index]:
                        bfs(i-1, j, index+1, 0)
            if prestep != 3:
                if j + 1 < len(board[0]):
                    if board[i][j+1] == word[index]:
                        bfs(i, j+1, index+1, 1)
            if prestep != 0:
                if i + 1 < len(board):
                    if board[i+1][j] == word[index]:
                        bfs(i+1, j, index+1, 2)
            if prestep != 1:
                if j - 1 >= 0:
                    if board[i][j-1] == word[index]:
                        bfs(i, j-1, index+1, 3)
            board[i][j] = tmp
            return
        
        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == word[0]):
                    bfs(i, j, 1, -1)
                    if (ans):
                        return True
        return False        
