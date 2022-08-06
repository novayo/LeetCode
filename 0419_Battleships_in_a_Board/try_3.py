class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        height, width = len(board), len(board[0])
        
        def mark(i, j):
            que = [(i, j)]
            board[i][j] = '.'
            
            while que:
                i, j = que.pop()
                
                for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                    if not (0 <= x < height and 0 <= y < width) or board[x][y] == '.':
                        continue
                    
                    board[x][y] = '.'
                    que.append((x, y))
                    
        ans = 0
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'X':
                    mark(i, j)
                    ans += 1
        return ans
