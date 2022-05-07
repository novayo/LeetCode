class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        def dfs(n, k):
            if n <= 1:
                return n
            if k == 1:
                return n
            
            if (n, k) not in memo:
                ret = float('inf')
                for a in range(n//2+1, 0, -1):
                    ret = min(
                        ret,
                        max(dfs(a-1, k-1), dfs(n-a, k))
                    )
                memo[n, k] = ret + 1
            return memo[n, k]
        
        return dfs(n, k)
