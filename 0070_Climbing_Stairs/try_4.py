class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        
        return b