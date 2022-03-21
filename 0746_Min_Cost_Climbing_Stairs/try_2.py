class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            c = cost[i] + min(a, b)
            a = b
            b = c
        
        return min(a, b)