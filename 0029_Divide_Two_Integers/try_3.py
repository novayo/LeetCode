class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        is_neg = (dividend > 0) ^ (divisor > 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        ans = 0
      
        while a >= b:
            # find_max_number_by_bit
            bit_for_b = 0
            while a >= (b << bit_for_b):
                bit_for_b += 1
            bit_for_b -= 1
            
            # Add quotient into ans
            ans += 1 << bit_for_b
            
            # Minus current b to a
            a -= b << bit_for_b
        
        return -ans if is_neg else ans
        