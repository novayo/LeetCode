class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        ans = 0
        queue = set()
        queue.add(n)
        
        while queue:
            next_queue = set()
            
            for _n in queue:
                if _n == 0:
                    return ans
                
                for square in squares:
                    if square <= _n:
                        next_queue.add(_n - square)
                    else:
                        break
            queue = next_queue
            ans += 1
        
        return ans
