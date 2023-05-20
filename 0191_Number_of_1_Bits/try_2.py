class Solution:
    def hammingWeight(self, n: int) -> int:
        
        def recr(l, r):
            if l < r:
                return 0
            if l == r:
                return n & (1 << l) != 0

            mid = l + (r - l) // 2
            if n <= 2**mid:
                return recr(mid-1, r) + ((n & (1 << mid)) != 0)
            else:
                return recr(l, mid+1) + ((n & (1 << mid)) != 0) + recr(mid-1, r)
            
        return recr(31, 0)