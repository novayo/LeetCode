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
            ans += 1
            tmp_queue = set()
            
            for remain in queue:
                for s in squares:
                    if remain == s:
                        return ans
                    elif remain < s:
                        break
                    else:
                        tmp_queue.add(remain-s)
            queue = tmp_queue
        
        return n