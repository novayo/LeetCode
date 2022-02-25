class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        cache = set()
        heap = [(-grid[0][0], 0, 0)]
        cur_min = float('inf')
        
        while heap:
            score, x, y = heapq.heappop(heap)
            score *= -1
            
            cur_min = min(cur_min, score)
            
            if x == height-1 and y == width-1:
                return cur_min
            
            for i, j in [x-1, y], [x+1, y], [x, y-1], [x, y+1]:
                if i < 0 or j < 0 or i >= height or j >= width or (i, j) in cache:
                    continue
                
                cache.add((i, j))
                heapq.heappush(heap, (-grid[i][j], i, j))
            
            
