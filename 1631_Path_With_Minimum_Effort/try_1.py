from sortedcontainers import SortedDict

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height = len(heights)
        width = len(heights[0])
        
        candidate = {(0, 0): 0}
        found = set()
        
        while candidate:
            cur_min = float('inf')
            x = y = -1
            for i, j in candidate.keys():
                if (i, j) in found:
                    continue
                if cur_min > candidate[i, j]:
                    cur_min = candidate[i, j]
                    x, y = i, j
            
            if x == -1 and y == -1:
                break
            
            found.add((x, y))
            
            for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                if i < 0 or j < 0 or i >= height or j >= width or (i, j) in found:
                    continue
                
                score = max(abs(heights[x][y] - heights[i][j]), candidate.get((x, y), 0))
                
                if (i, j) not in candidate or candidate[i, j] > score:
                    candidate[i, j] = score
        
        return candidate[height-1, width-1]
