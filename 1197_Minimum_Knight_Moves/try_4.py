class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def getScore(i, j):
            return (i-x)**2 + (j-y)**2
        
        heap = [(getScore(0, 0), 0, 0, 0)] # score, i, j, step
        found = set([(0, 0)])
        while heap:
            score, i, j, step = heapq.heappop(heap)
            
            if i == x and j == y:
                return step
            
            for _x, _y in [i+2, j+1], [i+2, j-1], [i+1, j+2], [i+1, j-2], [i-2, j+1], [i-2, j-1], [i-1, j+2], [i-1, j-2]:
                if (_x, _y) in found:
                    continue
                
                found.add((_x, _y))
                heapq.heappush(heap, (step*10+getScore(_x, _y), _x, _y, step+1))
                
