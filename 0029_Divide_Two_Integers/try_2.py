class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        
        ans = 0
        
        a = abs(dividend)
        b = abs(divisor)
        
        while a >= b:
            x = 0
            while a >= (b << x):
                x += 1
            x -= 1
            
            ans += 1 << x
            a -= b << x
        
        return -ans if (dividend > 0) ^ (divisor > 0) else ans
