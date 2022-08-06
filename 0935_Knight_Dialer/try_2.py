class Solution:
    def knightDialer(self, n: int) -> int:
        table = {
            0: [4,6], 
            1: [6,8], 
            2: [7,9], 
            3: [4,8], 
            4: [0,3,9], 
            5: [], 
            6: [0,1,7], 
            7: [2,6], 
            8: [1,3], 
            9: [2, 4]
        }
        
        @functools.lru_cache(None)
        def dfs(i, n):
            if n == 0:
                return 1
            return sum([dfs(nei, n-1) for nei in table[i]])
        
        MOD = 10**9+7
        return sum([dfs(i, n-1) % MOD for i in range(10)]) % MOD