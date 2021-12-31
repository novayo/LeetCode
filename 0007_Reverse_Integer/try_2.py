class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        
        is_neg = x < 0
        
        x = abs(x)
        while x:
            ans *= 10
            ans += x%10
            x //= 10
        
        if ans > 2**31-1:
            return 0
        return ans if not is_neg else -ans
