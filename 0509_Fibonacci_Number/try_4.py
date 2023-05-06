class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def recr(n):
            if n == 0:
                memo[n] = 0
                return memo[n]
            elif n == 1:
                memo[n] = 1
                return memo[n]
            
            if n in memo:
                return memo[n]
            
            memo[n] = recr(n-1) + recr(n-2)
            return memo[n]
        
        return recr(n)
    
