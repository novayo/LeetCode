class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        container = collections.defaultdict(int)
        
        # init
        for i in range(1, k+1):
            container[i] = 1
        
        for _n in range(1, n):
            next_container = collections.defaultdict(int)
            for key, value in container.items():
                for i in range(1, k+1):
                    if key+i > target:
                        break
                    next_container[key+i] = (next_container[key+i] + container[key]) % MOD
            container = next_container
        
        return container[target]
        
