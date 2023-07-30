class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0, k)] # (step, x, y, k)
        cache = {}
        
        while pq:
            step, x, y, cur_k = heapq.heappop(pq)
            
            if x == m-1 and y == n-1:
                return step
            
            for i, j in [x-1,y], [x+1,y], [x,y+1], [x,y-1]:
                if not (0 <= i < m and 0 <= j < n):
                    continue
                
                if (i, j) in cache and cache[i, j] >= cur_k:
                    continue

                if grid[i][j] == 0:
                    cache[i, j] = cur_k
                    heapq.heappush(pq, (step+1, i, j, cur_k))
                elif cur_k > 0:
                    cache[i, j] = cur_k-1
                    heapq.heappush(pq, (step+1, i, j, cur_k - 1))
        
        return -1
