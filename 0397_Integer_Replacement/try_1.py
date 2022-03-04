class Solution:
    def integerReplacement(self, n: int) -> int:
        
        memo = {}
        def recr(n):
            if n <= 1:
                return 0
            
            if n not in memo:
                if n % 2 == 0:
                    memo[n] = recr(n // 2) + 1
                else:
                    memo[n] = min(recr(n-1), recr(n+1)) + 1
            return memo[n]
        
        return recr(n)
