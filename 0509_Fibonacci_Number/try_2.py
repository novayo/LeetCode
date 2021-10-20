class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a = 0
        b = 1
        c = a + b
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        
        return c