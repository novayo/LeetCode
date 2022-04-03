class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        ans = float('inf')
        def recr(i, cur):
            nonlocal ans
            
            if abs(cur-target) < abs(ans-target) \
               or (abs(cur-target) == abs(ans-target) and cur < ans):
                ans = cur
            
            if i >= len(toppingCosts):
                return
            
            for n in range(3):
                recr(i+1, cur+n*toppingCosts[i])
        
        for base in baseCosts:
            recr(0, base)
        
        return ans
