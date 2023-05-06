class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recr(n):
            if n <= 2:
                memo[n] = n
                return memo[n]
            
            if n in memo:
                return memo[n]
            
            memo[n] = recr(n-1) + recr(n-2)
            return memo[n]
            
        return recr(n)
