class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        found = set()
        found.add((0, 0))
        
        queue = [(0, 0)]
        ans = 0
        while queue:
            next_queue = []
            
            while queue:
                i, j = queue.pop()
                
                if i == x and j == y:
                    return ans
            
                for _x, _y in [i+2, j+1], [i+2, j-1], [i+1, j+2], [i+1, j-2], [i-2, j+1], [i-2, j-1], [i-1, j+2], [i-1, j-2]:
                    if (_x, _y) in found:
                        continue
                    
                    found.add((_x, _y))
                    next_queue.append((_x, _y))
            
            ans += 1
            queue = next_queue
                
