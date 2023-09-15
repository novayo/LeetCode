class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def get_score(step, x, y):
            return step + ((height-1-x) + (width-1-y)) * 1.5
        height, width = len(grid), len(grid[0])
        pq = [(get_score(0, 0, 0), 0, -k, 0, 0)] # score, step, k, x, y
        done_set = set()
        
        while pq:
            score, step, cur_k, x, y = heapq.heappop(pq)
            cur_k *= -1

            if (cur_k, x, y) in done_set:
                continue

            if x == height-1 and y == width-1:
                return step
            
            done_set.add((cur_k, x, y))
            for i, j in [x,y-1],[x,y+1],[x+1,y],[x-1,y]:
                if not (0 <= i < height and 0 <= j < width):
                    continue
                
                if (cur_k, i, j) in done_set:
                    continue
                
                _k = cur_k
                if grid[i][j] == 1:
                    if _k == 0:
                        continue
                    _k -= 1
                
                heapq.heappush(pq, (get_score(step+1, i, j), step+1, -_k, i, j))
        
        return -1
