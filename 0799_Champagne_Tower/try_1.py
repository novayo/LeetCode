class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        memo = {}
        def dfs(x, y):
            
            if x < 0 or y < 0:
                return 0
            
            if x == 0 and y == 0:
                return poured
            
            if (x, y) not in memo:
                memo[x, y] = max(0, (dfs(x-1, y)-1)/2) + max(0, (dfs(x-1, y-1)-1)/2)
            return memo[x, y]
        
        ans = dfs(query_row, query_glass) 
        return ans if ans < 1 else 1
