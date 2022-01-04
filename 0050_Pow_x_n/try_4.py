class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = {}
        
        def dfs(n):
            
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n == -1:
                return 1/x
            
            memo[n] = dfs(n//2) * dfs(n-n//2)
            return memo[n]
        
        return dfs(n)
