class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        cache = {}
        max_heap = [(-grid[0][0], 0, 0)] # score, i, j
        
        while max_heap:
            cur_score, i, j = heapq.heappop(max_heap)
            cur_score *= -1
            
            if i == height-1 and j == width-1:
                return cur_score
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width):
                    continue
                
                score = min(cur_score, grid[x][y])
                if cache.get((x, y), -float('inf')) >= score:
                    continue
                
                cache[x, y] = score
                heapq.heappush(max_heap, (-score, x, y))
        
        return -1