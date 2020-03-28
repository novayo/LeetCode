class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        x = y = 0
        endx = len(grid) - 1
        endy = len(grid[0]) - 1
        
        # 0 up
        # 1 right
        # 2 down
        # 3 left
        face = -1
        if grid[x][y] == 1:
            face = 1
        elif grid[x][y] == 2:
            face = 2
        elif grid[x][y] == 3:
            face = 2
            x += 1
        elif grid[x][y] == 4:
            face = 2
            x += 1
        elif grid[x][y] == 5:
            face = 3
            
        elif grid[x][y] == 6:
            face = 1
            y += 1
        else:
            return False
        
        went = set((0,0))
        while x != endx or y != endy:
            # print(x, y)
            if (x,y) in went:
                return False
            went.add((x,y))
            
            if grid[x][y] == 1:
                if face == 1:
                    x = x
                    y = y + 1
                elif face == 3:
                    x = x
                    y = y - 1
                else:
                    return False
            elif grid[x][y] == 2:
                if face == 2:
                    x = x + 1
                    y = y
                elif face == 0:
                    x = x - 1
                    y = y
                else:
                    return False
            elif grid[x][y] == 3:
                if face == 1:
                    x = x + 1
                    y = y
                    face = 2
                elif face == 0:
                    x = x - 1
                    y = y
                    face = 3
                else:
                    return False
            elif grid[x][y] == 4:
                if face == 0:
                    x = x
                    y = y + 1
                    face = 1
                elif face == 3:
                    x = x + 1
                    y = y
                    face = 2
                else:
                    return False
            elif grid[x][y] == 5:
                if face == 2:
                    x = x
                    y = y - 1
                    face = 3
                elif face == 1:
                    x = x - 1
                    y = y
                    face = 0
                else:
                    return False
            elif grid[x][y] == 6:
                if face == 2:
                    x = x
                    y = y + 1
                    face = 1
                elif face == 3:
                    x = x - 1
                    y = y
                    face = 0
                else:
                    return False
            
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
        
        # print("asdas")
        if grid[x][y] == 1:
                if face == 1:
                    x = x
                    y = y + 1
                elif face == 3:
                    x = x
                    y = y - 1
                else:
                    return False
        elif grid[x][y] == 2:
            if face == 2:
                x = x + 1
                y = y
            elif face == 0:
                x = x - 1
                y = y
            else:
                return False
        elif grid[x][y] == 3:
            if face == 1:
                x = x + 1
                y = y
                face = 2
            elif face == 0:
                x = x - 1
                y = y
                face = 3
            else:
                return False
        elif grid[x][y] == 4:
            if face == 0:
                x = x
                y = y + 1
                face = 1
            elif face == 3:
                x = x + 1
                y = y
                face = 2
            else:
                return False
        elif grid[x][y] == 5:
            if face == 2:
                x = x
                y = y - 1
                face = 3
            elif face == 1:
                x = x - 1
                y = y
                face = 0
            else:
                return False
        elif grid[x][y] == 6:
            if face == 2:
                x = x
                y = y + 1
                face = 1
            elif face == 3:
                x = x - 1
                y = y
                face = 0
            else:
                return False
        return True
