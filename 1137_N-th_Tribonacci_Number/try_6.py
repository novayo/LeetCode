class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def recr(n):
            if n <= 1:
                memo[n] = n
                return memo[n]
            elif n == 2:
                memo[n] = 1
                return memo[n]
            
            if n in memo:
                return memo[n]
            
            memo[n] = recr(n-1) + recr(n-2) + recr(n-3)
            return memo[n]
        
        return recr(n)

