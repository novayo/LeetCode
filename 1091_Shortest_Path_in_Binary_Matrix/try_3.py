class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        height, width = len(grid), len(grid[0])
        pq = [(1, 0, 0)] # step, x, y
        done_set = set()
        
        while pq:
            step, x, y = heapq.heappop(pq)
            
            if x == height-1 and y == width-1:
                return step
            
            for i, j in [x-1,y],[x-1,y-1],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]:
                if not (0 <= i < height and 0 <= j < width):
                    continue
                
                if grid[i][j] == 1:
                    continue
                
                if (i, j) in done_set:
                    continue
                
                heapq.heappush(pq, (step+1, i, j))
                done_set.add((i, j))
        
        return -1

