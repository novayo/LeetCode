class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        pq = [(1, 0, 0)] # step, x, y
        cache = {}
        
        while pq:
            step, x, y = heapq.heappop(pq)
            
            if x == m-1 and y == n-1:
                return step
            
            for i, j in [x-1,y],[x-1,y-1],[x-1,y+1],[x,y+1],[x,y-1],[x+1,y+1],[x+1,y],[x+1,y-1]:
                if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 1:
                    continue
                
                cur_step = step + 1
                
                if cache.get((i, j), float('inf')) <= cur_step:
                    continue
                
                cache[i,j] = cur_step
                heapq.heappush(pq, (cur_step, i, j))
        
        return -1

