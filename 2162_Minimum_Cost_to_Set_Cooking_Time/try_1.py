class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        '''
        依樣的話，可以直接push (到任一值)
        不一樣的話，要先move再push (到任一值)
        1006
        106
        '''
        def cal_cost(m, s):
            time = str(m) + str(s).zfill(2)
            time = time.lstrip('0')
            current = str(startAt)
            cost = 0
            
            for t in time:
                if t != current:
                    cost += moveCost
                    current = t
                cost += pushCost
            return cost
        
        
        ans = float('inf')
        for m in range(100):
            for s in range(100):
                if m*60 + s > targetSeconds:
                    break
                if m*60 + s == targetSeconds:
                    ans = min(ans, cal_cost(m, s))
        return ans
