class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(baseCosts)
        m = len(toppingCosts)
        
        def recr(idx, cost, trail):
            if abs(target-cost) < abs(target-trail[0]):
                trail[0] = cost
            elif abs(target-cost) == abs(target-trail[0]):
                trail[0] = min(trail[0], cost)
            
            if idx >= m:
                return
            
            for k in range(3):
                recr(idx+1, cost + toppingCosts[idx] * k, trail)
                    
        
        ans = float('inf')
        for base in baseCosts:
            trail = [ans]
            recr(0, base, trail)
            if abs(target-trail[0]) < abs(target-ans):
                ans = trail[0]
            elif abs(target-trail[0]) == abs(target-ans):
                ans = min(ans, trail[0])
        
        return ans