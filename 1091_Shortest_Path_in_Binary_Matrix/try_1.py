class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def dist(i, j):
            return (height-i) + (width-j)
        
        if grid[0][0] == 1:
            return -1
        
        height, width = len(grid), len(grid[0])
        cache = {(0, 0): 1}
        heap = [(1, 0, 0)]
        
        while heap:
            step, i, j = heapq.heappop(heap)
            
            if i == height-1 and j == width-1:
                return step
            
            for x, y in [i-1, j], [i-1, j+1], [i, j+1], [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1], [i-1, j-1]:
                if x < 0 or y < 0 or x >= height or y >= width \
                   or grid[x][y] == 1 or cache.get((x, y), float('inf')) <= step+1:
                    continue
                
                cache[x, y] = step+1
                heapq.heappush(heap, (step+1, x, y))
        
        return -1
