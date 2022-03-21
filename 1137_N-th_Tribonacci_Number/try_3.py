class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b, c = 0, 1, 1
        for i in range(n-2):
            d = a + b + c
            a = b
            b = c
            c = d
        
        return c