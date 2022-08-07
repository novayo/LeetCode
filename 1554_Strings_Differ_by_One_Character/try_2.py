class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        MOD = sys.maxsize
        
        rolling_hash = [0] * n
        for i in range(n):
            for j in range(m):
                rolling_hash[i] = (rolling_hash[i] * 26 + (ord(dict[i][j]) - ord('a'))) % MOD
        
        
        base = 0
        for j in range(m-1, -1, -1):
            cache = set()
            for i in range(n):
                marked = (rolling_hash[i] - (ord(dict[i][j]) - ord('a')) * pow(26, base, MOD)) % MOD
                if marked in cache:
                    return True
                cache.add(marked)
            base += 1
        
        return False
