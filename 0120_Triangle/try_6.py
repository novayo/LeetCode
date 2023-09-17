class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        
        def recr(layer, i):
            if layer == n:
                return 0
            
            if (layer, i) in memo:
                return memo[layer, i]
            
            memo[layer, i] = triangle[layer][i] + min(
                recr(layer+1, i),
                recr(layer+1, i+1)
            )
            return memo[layer, i]
        
        return recr(0, 0)
            
        
