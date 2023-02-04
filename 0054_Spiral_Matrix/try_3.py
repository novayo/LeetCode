LEFT, RIGHT, DOWN, TOP = 0, 1, 2, 3
VISITED = -float('inf')

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        turn = RIGHT
        x, y = 0, 0
        ans = []
        
        while 0 <= x < m and 0 <= y < n and matrix[x][y] != VISITED:
            ans.append(matrix[x][y])
            matrix[x][y] = VISITED
            
            if turn == RIGHT:
                if y == n-1 or matrix[x][y+1] == VISITED:
                    x += 1
                    turn = DOWN
                else:
                    y += 1
            elif turn == DOWN:
                if x == m-1 or matrix[x+1][y] == VISITED:
                    turn = LEFT
                    y -= 1
                else:
                    x += 1
            elif turn == LEFT:
                if y == 0 or matrix[x][y-1] == VISITED:
                    turn = TOP
                    x -= 1
                else:
                    y -= 1
            else:
                if x == 0 or matrix[x-1][y] == VISITED:
                    turn = RIGHT
                    y += 1
                else:
                    x -= 1
        return ans

