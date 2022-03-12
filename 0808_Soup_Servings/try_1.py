class Solution:
    def soupServings(self, n: int) -> float:
        
        if n >= 5000:
            return 1
        
        memo = {}
        def recr(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            
            if (a, b) not in memo:
                memo[a, b] = 0.25 * (recr(a-100, b) + recr(a-75, b-25) + recr(a-50, b-50) + recr(a-25, b-75))
            return memo[a, b]
        
        return recr(n, n)
