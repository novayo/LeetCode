class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red = blue = green = 0
        
        for r, b, g in costs:
            next_red = r + min(blue, green)
            next_blue = b + min(red, green)
            next_green = g + min(red, blue)
            
            red, blue, green = next_red, next_blue, next_green
        
        return min(red, blue, green)