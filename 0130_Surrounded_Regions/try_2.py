class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs
        visited = collections.defaultdict(bool)
        
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or\
               visited.get((i, j)) or board[i][j] == 'X':
                return
            visited[i, j] = True
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
                
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == 'O' and not visited[i, j]:
                    board[i][j] = 'X'
