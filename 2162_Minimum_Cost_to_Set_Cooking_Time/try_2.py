class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        @functools.lru_cache(None)
        def helper(m, s):
            time = str(m) + str(s).zfill(2)
            time = time.lstrip('0')
            ret = 0
            cur = startAt
            
            for t in time:
                if t != cur:
                    ret += moveCost
                ret += pushCost
                cur = t
            return ret
            
        startAt = str(startAt)
        ans = float('inf')
        for m in range(100):
            for s in range(100):
                if m*60 + s > targetSeconds:
                    break
                
                if m*60 + s == targetSeconds:
                    ans = min(ans, helper(m, s))
        return ans
