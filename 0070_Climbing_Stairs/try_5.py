class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recr(n):
            if n <= 2:
                return n
            
            return recr(n-1) + recr(n-2)
            
        return recr(n)
