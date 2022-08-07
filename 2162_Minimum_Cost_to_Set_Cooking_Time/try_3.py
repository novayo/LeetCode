class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def helper(m, s):
            target_string = str(m) + str(s).zfill(2)
            while target_string[0] == '0':
                target_string = target_string[1:]
            
            ret = 0
            cur = str(startAt)
            for t in target_string:
                if t != cur:
                    ret += moveCost
                ret += pushCost
                cur = t
            return ret
            
        
        ans = float('inf')
        for m in range(100):
            for s in range(100):
                if m * 60 + s == targetSeconds:
                    ans = min(ans, helper(m, s))
        return ans
        
