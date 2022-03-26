class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs) // 2
        
        memo = {}
        def recr(index, a=n, b=n):
            if a < 0 or b < 0:
                return float('inf')
            if a == 0 and b == 0:
                return 0
            
            if (a, b) not in memo:
                memo[a, b] = min(
                    costs[index][0] + recr(index+1, a-1, b),
                    costs[index][1] + recr(index+1, a, b-1)
                )
            return memo[a, b]
        
        return recr(0)
            
