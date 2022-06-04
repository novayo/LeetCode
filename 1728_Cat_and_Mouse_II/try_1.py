class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        def allParents(mx, my, cx, cy, who):
            ret = []
            if who == 1:
                for ox, oy in [1, 0], [-1, 0], [0, 1], [0, -1]:
                    for i in range(catJump+1):
                        x, y = cx + i*ox, cy + i*oy
                        if not (0 <= x < height and 0 <= y < width):
                            break
                        
                        if grid[x][y] == '#':
                            break
                        
                        ret.append((mx, my, x, y, 2))
            else:
                for ox, oy in [1, 0], [-1, 0], [0, 1], [0, -1]:
                    for i in range(mouseJump+1):
                        x, y = mx + i*ox, my + i*oy
                        if not (0 <= x < height and 0 <= y < width):
                            break
                        
                        if grid[x][y] == '#':
                            break
                        
                        ret.append((x, y, cx, cy, 1))
            return ret
        
        def allChildrenWin(mx, my, cx, cy, who):
            if who == 1:
                for ox, oy in [1, 0], [-1, 0], [0, 1], [0, -1]:
                    for i in range(mouseJump+1):
                        x, y = mx + i*ox, my + i*oy
                        if not (0 <= x < height and 0 <= y < width):
                            break
                        
                        if grid[x][y] == '#':
                            break
                        
                        if status[x, y, cx, cy, 2] != 2:
                            return False
            else:
                for ox, oy in [1, 0], [-1, 0], [0, 1], [0, -1]:
                    for i in range(catJump+1):
                        x, y = cx + i*ox, cy + i*oy
                        if not (0 <= x < height and 0 <= y < width):
                            break
                        
                        if grid[x][y] == '#':
                            break
                        
                        if status[mx, my, x, y, 1] != 1:
                            return False
            return True
        
        height = len(grid)
        width = len(grid[0])
        
        # get pos
        mouse = cat = food = None
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)
                elif grid[i][j] == 'F':
                    food = (i, j)
        
        # init
        status = collections.defaultdict(int)
        que = collections.deque()
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '#':
                    continue
                
                #   if mouse gets food
                status[food[0], food[1], i, j, 1] = 1
                status[food[0], food[1], i, j, 2] = 1
                que.append((food[0], food[1], i, j, 1))
                que.append((food[0], food[1], i, j, 2))
                
                #   if cat gets food
                status[i, j, food[0], food[1], 1] = 2
                status[i, j, food[0], food[1], 2] = 2
                que.append((i, j, food[0], food[1], 1))
                que.append((i, j, food[0], food[1], 2))
                
                #   if cat == mouse
                status[i, j, i, j, 1] = 2
                status[i, j, i, j, 2] = 2
                que.append((i, j, i, j, 1))
                que.append((i, j, i, j, 2))
        
        # bfs
        layer = 0
        while que:
            next_queue = collections.deque()
            for mx, my, cx, cy, who in que:
                s = status[mx, my, cx, cy, who]
                for mx2, my2, cx2, cy2, who2 in allParents(mx, my, cx, cy, who):
                    if status[mx2, my2, cx2, cy2, who2] != 0:
                        continue

                    if s == who2:
                        status[mx2, my2, cx2, cy2, who2] = s
                        next_queue.append((mx2, my2, cx2, cy2, who2))
                    elif allChildrenWin(mx2, my2, cx2, cy2, who2):
                        status[mx2, my2, cx2, cy2, who2] = 1 if who2 == 2 else 2
                        next_queue.append((mx2, my2, cx2, cy2, who2))

            que = next_queue
            layer += 1
            if layer >= 1000:
                break
        
        return status[mouse[0], mouse[1], cat[0], cat[1], 1] == 1
