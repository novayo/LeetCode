class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        for layer in range(n-2, -1, -1):
            for i in range(len(triangle[layer])):
                triangle[layer][i] += min(
                    triangle[layer+1][i], triangle[layer+1][i+1], 
                )
        
        return triangle[0][0]

    
