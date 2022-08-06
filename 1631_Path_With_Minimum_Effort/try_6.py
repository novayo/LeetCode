class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height, width = len(heights), len(heights[0])
        cache = {(0, 0): 0}
        pq = [(0, 0, 0)]
        
        while pq:
            effort, i, j = heapq.heappop(pq)
            
            if (i, j) == (height-1, width-1):
                return effort
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width):
                    continue
                
                new_effort = max(effort, abs(heights[i][j] - heights[x][y]))
                
                if cache.get((x, y), float('inf')) <= new_effort:
                    continue
                
                cache[x, y] = new_effort
                heapq.heappush(pq, (new_effort, x, y))
        
        return -1
        
