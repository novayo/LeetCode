class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for layer in range(len(triangle)-2, -1, -1):
            for i in range(layer+1):
                triangle[layer][i] += min(triangle[layer+1][i], triangle[layer+1][i+1])
        
        return triangle[0][0]