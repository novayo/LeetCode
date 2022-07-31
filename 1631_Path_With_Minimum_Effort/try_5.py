class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height, width = len(heights), len(heights[0])
        cache = set()
        que = []
        
        # init
        que.append((0, 0, 0)) # score, x, y
        
        # bfs
        while que:
            diff, x, y = heapq.heappop(que)
            
            if x == height-1 and y == width-1:
                return diff
            
            if (x, y) in cache:
                continue
            cache.add((x, y))
            
            for i, j in [x-1,y], [x+1,y], [x,y-1], [x,y+1]:
                if not (0 <= i < height and 0 <= j < width):
                    continue
                heapq.heappush(que, (max(diff, abs(heights[i][j] - heights[x][y])), i, j))
        
        return -1    
