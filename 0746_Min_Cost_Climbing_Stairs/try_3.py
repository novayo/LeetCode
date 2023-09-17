class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def recr(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(recr(i+1), recr(i+2))
            return memo[i]
        
        return min(recr(0), recr(1))
