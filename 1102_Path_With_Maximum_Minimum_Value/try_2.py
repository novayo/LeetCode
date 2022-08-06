class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        cache = {(0, 0): grid[0][0]}
        min_heap = [(-grid[0][0], 0, 0)] # cur_min, i, j
        
        while min_heap:
            cur_min, i,j = heapq.heappop(min_heap)
            cur_min *= -1
            
            if (i, j) == (height-1, width-1):
                return cur_min
            
            for x, y in [i-1, j], [i+1, j], [i, j+1], [i, j-1]:
                if not (0 <= x < height and 0 <= y < width):
                    continue
                    
                score = min(cur_min, grid[x][y])
                
                if cache.get((x, y), -float('inf')) >= score:
                    continue
                
                heapq.heappush(min_heap, (-score, x, y))
                cache[x, y] = score
        
        return -1
