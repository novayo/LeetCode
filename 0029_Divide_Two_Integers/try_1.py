class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # https://www.youtube.com/watch?v=htX69j1jf5U
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        
        a, b, res = abs(dividend), abs(divisor), 0
        
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
                
        return res if (dividend > 0) == (divisor > 0) else ~res+1
