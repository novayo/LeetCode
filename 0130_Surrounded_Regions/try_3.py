class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs
        visited = {}
        
        def dfs(i, j):
            if visited.get((i, j)) or board[i][j] == 'X':
                return
            visited[i, j] = True
            if j-1 > 0: dfs(i, j-1) # 上
            if i+1 < len(board): dfs(i+1, j) # 右
            if j+1 < len(board[0]): dfs(i, j+1) # 下
            if i-1 > 0: dfs(i-1, j) # 左

        for i in range(len(board)):
            if i == 0 or i == len(board)-1:
                for j in range(len(board[0])):
                    dfs(i, j)
            else:
                dfs(i, 0)
                dfs(i, len(board[0])-1)
                
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == 'O' and not visited.get((i,j)):
                    board[i][j] = 'X'
