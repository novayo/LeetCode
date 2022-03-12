UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def getPos(i, j, face):
            for _ in range(4):
                if face == UP:
                    x, y = i-1, j
                elif face == LEFT:
                    x, y = i, j-1
                elif face == DOWN:
                    x, y = i+1, j
                else:
                    x, y = i, j+1

                if x < 0 or y < 0 or x >= n or y >= n or (x, y) in cache:
                    face = (face+1) % 4
                else:
                    return x, y, face
        
        dp = [[0] * n for _ in range(n)]
        
        cache = set()
        i = j = 0
        face = RIGHT
        for _n in range(1, n**2):
            cache.add((i, j))
            dp[i][j] = _n
            i, j, face = getPos(i, j, face)
        dp[i][j] = n**2
        return dp
