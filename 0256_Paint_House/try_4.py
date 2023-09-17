class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        memo = {}

        def recr(i, prev_choice):
            if i == n:
                return 0
            
            if (i, prev_choice) in memo:
                return memo[i, prev_choice]

            ans = float('inf')
            for j in range(3):
                if j == prev_choice:
                    continue
                
                ans = min(ans, costs[i][j] + recr(i+1, j))

            memo[i, prev_choice] = ans
            return memo[i, prev_choice]
        
        return recr(0, -1)

