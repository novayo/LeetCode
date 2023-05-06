class Solution:
    def tribonacci(self, n: int) -> int:
        
        def recr(n):
            if n <= 1:
                return n
            elif n == 2:
                return 1
            
            return recr(n-1) + recr(n-2) + recr(n-3)
        
        return recr(n)

