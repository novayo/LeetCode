class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = {}
        pq = [(-grid[0][0], 0, 0)] # score, x, y

        while pq:
            score, x, y = heapq.heappop(pq)
            score *= -1

            if x == m-1 and y == n-1:
                return score
            
            for i, j in [x,y-1], [x,y+1], [x+1,y], [x-1,y]:
                if not (0 <= i < m and 0 <= j < n):
                    continue
                
                cur_score = min(grid[i][j], score)

                if cache.get((i, j), -float('inf')) >= cur_score:
                    continue
                
                cache[i, j] = cur_score
                heapq.heappush(pq, (-cur_score, i, j))
        
        return -1

