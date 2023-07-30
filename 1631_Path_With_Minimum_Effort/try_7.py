class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)] # diff, x, y
        cache = {}
        
        while pq:
            diff, x, y = heapq.heappop(pq)
            
            if x == m-1 and y == n-1:
                return diff
            
            for i, j in [x,y+1],[x,y-1],[x+1,y],[x-1,y]:
                if not (0 <= i < m and 0 <= j < n):
                    continue
                _diff = max(diff, abs(heights[x][y] - heights[i][j]))
                if cache.get((i,j), float('inf')) > _diff:
                    cache[i,j] = _diff
                    heapq.heappush(pq, (_diff, i, j))
        
        return -1
