class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs
        # self.printAll(board)
        
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or board[i][j] == 'X' or board[i][j] == 'Q':
                return
            board[i][j] = 'Q'
            dfs(i, j-1) # 上
            dfs(i+1, j) # 右
            dfs(i, j+1) # 下
            dfs(i-1, j) # 左

        for i in range(len(board)):
            if i == 0 or i == len(board)-1:
                for j in range(len(board[0])):
                    dfs(i, j)
            else:
                dfs(i, 0)
                dfs(i, len(board[0])-1)
                
        # self.printAll(board)
        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == 'Q': board[i][j] = 'O'
                elif b == 'O': board[i][j] = 'X'
        # self.printAll(board)
        
    def printAll(self, board):
        for b in board:
            print(' '.join(b))
        print("---------")
