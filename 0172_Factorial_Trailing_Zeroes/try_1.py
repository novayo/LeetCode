class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        tmp = 5
        
        while tmp <= n:
            ans += n // tmp
            tmp *= 5
        
        return ans
