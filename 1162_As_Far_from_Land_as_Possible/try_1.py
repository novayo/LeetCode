class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # define
        height, width = len(grid), len(grid[0])
        visited = set()
        min_heap = []
        
        # init
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    min_heap.append((0, i, j))
        
        # if 1 doesn't exist
        if len(min_heap) == 0:
            return -1
        
        # dijstra
        ans = -1
        while min_heap:
            score, i, j = heapq.heappop(min_heap)
            
            ans = max(ans, score)
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height) or not (0 <= y < width) or (x, y) in visited:
                    continue
                
                visited.add((x, y))
                heapq.heappush(min_heap, (score+1, x, y))
        
        return ans if ans > 0 else -1