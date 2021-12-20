class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height = len(heights)
        width = len(heights[0])
        
        dp = {(0, 0): 0}
        candidate = {(0, 0): 0}
        found = set()
        
        while candidate:
            cur_min = float('inf')
            x = y = -1
            for i, j in candidate.keys():
                if cur_min > candidate[i, j]:
                    cur_min = candidate[i, j]
                    x, y = i, j
            
            del candidate[x, y]
            found.add((x, y))
            
            for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                if i < 0 or j < 0 or i >= height or j >= width or (i, j) in found:
                    continue
                
                score = max(abs(heights[x][y] - heights[i][j]), dp.get((x, y), 0))
                
                if (i, j) not in dp or candidate[i, j] > score:
                    candidate[i, j] = score
                    dp[i, j] = score
        
        return dp[height-1, width-1]
