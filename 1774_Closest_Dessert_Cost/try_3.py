class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(baseCosts)
        m = len(toppingCosts)
        ans = float('inf')

        def recr(idx, cost):
            nonlocal ans
            
            if abs(target-cost) < abs(target-ans):
                ans = cost
            elif abs(target-cost) == abs(target-ans):
                ans= min(ans, cost)
            
            if idx >= m or cost - target > ans:
                return
            
            for k in range(3):
                recr(idx+1, cost + toppingCosts[idx] * k)
        
        for base in baseCosts:
            recr(0, base)
        
        return ans