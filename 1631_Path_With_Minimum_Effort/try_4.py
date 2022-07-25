class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height, width = len(heights), len(heights[0])
        cache = {(0, 0): 0}
        min_heap = [(0, 0, 0)] # (cur_effort, x, y)
        
        while min_heap:
            cur_effort, x, y = heapq.heappop(min_heap)
            
            if x == height-1 and y == width-1:
                return cur_effort
            
            for i, j in [x-1,y], [x+1,y], [x,y-1], [x,y+1]:
                if not (0 <= i < height and 0 <= j < width):
                    continue
                    
                cur = max(cur_effort, abs(heights[x][y] - heights[i][j]))
                    
                if cur >= cache.get((i, j), float('inf')):
                    continue
                    
                heapq.heappush(min_heap, (cur, i, j))
                cache[i, j] = cur
        
        return -1
