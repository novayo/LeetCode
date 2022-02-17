class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        dp => dp[pos] = current min
        dijatra
        '''
        height = len(heights)
        width = len(heights[0])
        heap = []
        dp = collections.defaultdict(lambda: float('inf'))
        
        
        # init
        heap.append((0, 0, 0))
        dp[0, 0] = 0
        
        # loop
        while heap:
            current_diff, x, y = heapq.heappop(heap)
            
            if x == height-1 and y == width-1:
                return current_diff
            
            for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                if i < 0 or j < 0 or i >= height or j >= width:
                    continue
                
                diff = max(current_diff, abs(heights[i][j] - heights[x][y]))
                
                if diff < dp[i, j]:
                    heapq.heappush(heap, (diff, i, j))
                    dp[i, j] = diff
