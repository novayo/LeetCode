class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        
        doable = {
            1: {RIGHT: {1, 3, 5}, LEFT: {1, 4, 6}},
            2: {UP: {2, 3, 4}, DOWN: {2, 5, 6}},
            3: {DOWN: {2, 5, 6}, LEFT: {1, 4, 6}},
            4: {RIGHT: {1, 3, 5}, DOWN: {2, 5, 6}},
            5: {UP: {2, 3, 4}, LEFT: {1, 4, 6}},
            6: {UP: {2, 3, 4}, RIGHT: {1, 3, 5}},
        }
        
        height, width = len(grid), len(grid[0])
        
        if grid[0][0] == 1:
            trials = [0, 1]
        
        for trial in range(2):
            x, y = 0, 0
            cache = set()
            while True:
                street = grid[x][y]

                if x == height-1 and y == width-1:
                    return True

                if (x, y) in cache:
                    break
                cache.add((x, y))

                for direction in sorted(doable[street].keys(), reverse=trial==1):
                    possible = doable[street][direction]
                    if direction == UP:
                        i, j = x-1, y
                    elif direction == RIGHT:
                        i, j = x, y+1
                    elif direction == DOWN:
                        i, j = x+1, y
                    else:
                        i, j = x, y-1

                    if i < 0 or j < 0 or i >= height or j >= width or (i, j) in cache or grid[i][j] not in possible:
                        continue

                    x, y = i, j
                    break
        
        return False