class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        
        ans = 0
        found = set()
        found.add((0, 0))
        queue = set()
        queue.add((0, 0))
        while queue:
            next_queue = set()
            
            for i, j in queue:
                
                if i == x and j == y:
                    return ans
                
                for _x, _y in [i+2, j+1], [i+2, j-1], [i+1, j+2], [i+1, j-2], [i-2, j+1], [i-2, j-1], [i-1, j+2], [i-1, j-2]:
                    if _x < -2 or _y < -2 or (_x, _y) in found:
                        continue
                    found.add((_x, _y))
                    next_queue.add((_x, _y))
            
            ans += 1
            queue = next_queue
                    
