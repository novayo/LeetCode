class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        bfs
        '''
        FIRST_LAND = -1
        height, width = len(grid), len(grid[0])
        
        def changeFirstLand(i, j, container):
            if not (0 <= i < height) or not (0 <= j < width) or grid[i][j] != 1:
                return
            
            grid[i][j] = FIRST_LAND
            container.append((i, j))
            
            for x, y in [i+1, j], [i-1, j], [i, j+1], [i, j-1]:
                changeFirstLand(x, y, container)
        
        # find first land
        container = []
        flag = False
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    changeFirstLand(i, j, container)
                    flag = True
                    break
            if flag:
                break
        
        # bfs
        ans = 0
        while container:
            next_container = []
            
            for i, j in container:
                for x, y in [i+1, j], [i-1, j], [i, j+1], [i, j-1]:
                    if not (0 <= x < height) or not (0 <= y < width) or grid[x][y] == FIRST_LAND:
                        continue
                    if grid[x][y] == 1:
                        return ans
                    
                    grid[x][y] = FIRST_LAND
                    next_container.append((x, y))
            
            ans += 1
            container = next_container
             
