class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        height = len(board)
        width = len(board[0])
        
        queue = collections.deque()
        visited = set()
        
        # init
        queue.appendleft(click)
        visited.add(tuple(click))
        
        # bfs
        while queue:
            i, j = queue.pop()
            
            # check if click on a mine
            if board[i][j] == 'M':
                board[i][j] = 'X'
                break
            
            # check if any mine around (i, j)
            mines = 0
            for x, y in [i-1, j-1], [i-1, j], [i-1, j+1], [i, j+1], [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1]:
                if (not (0 <= x < height and 0 <= y < width)):
                    continue
                if board[x][y] == 'M':
                    mines += 1
            
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                for x, y in [i-1, j-1], [i-1, j], [i-1, j+1], [i, j+1], [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1]:
                    if (not (0 <= x < height and 0 <= y < width)):
                        continue
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    queue.appendleft((x, y))
        
        return board
            