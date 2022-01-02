class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        ans = 0
        
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            
            left = right = float('inf')
            if index > 0:
                left = house - heaters[index-1]
                
            if index < len(heaters):
                right = heaters[index] - house
            
            ans = max(ans, min(left, right))
        
        return ans
        
