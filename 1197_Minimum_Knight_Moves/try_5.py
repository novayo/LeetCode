class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        pq = [(0, 0, 0)] # step, x, y
        done_set = set()
        done_set.add((0, 0))

        while pq:
            step, i, j = heapq.heappop(pq)

            if i == x and j == y:
                return step
            
            for _i, _j in [i-1, j-2], [i-1, j+2], [i-2, j-1], [i-2, j+1], [i+1, j-2], [i+1, j+2], [i+2, j-1], [i+2, j+1]:
                if (_i, _j) in done_set:
                    continue
                
                heapq.heappush(pq, (step+1, _i, _j))
                done_set.add((_i, _j))

