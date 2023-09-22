class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def recr(i):
            if i <= 1:
                return i
            
            if i in memo:
                return memo[i]
            
            memo[i] = recr(i-1) + recr(i-2) 
            return memo[i]
        
        return recr(n)
