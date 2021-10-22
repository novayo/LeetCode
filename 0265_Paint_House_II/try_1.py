class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            a = b = float('inf')
            
            for cost in costs[i-1]:
                if cost > b:
                    continue
                elif b > cost > a:
                    b = cost
                elif a >= cost:
                    b = a
                    a = cost
            
            for j in range(len(costs[i-1])):
                if costs[i-1][j] != a:
                    costs[i][j] += a
                else:
                    costs[i][j] += b
        
        return min(costs[-1])