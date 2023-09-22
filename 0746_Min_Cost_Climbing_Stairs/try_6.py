class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        a, b = cost[0], cost[1]
        
        for i in range(2, n):
            c = min(a, b) + cost[i]
            a = b
            b = c
        
        return min(a, b)
        
