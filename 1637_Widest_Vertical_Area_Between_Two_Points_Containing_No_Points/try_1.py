class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        valid_x = set()
        for x, y in points:
            valid_x.add(x)
        
        ans = 0
        previous_x = -float('inf')
        for x in sorted(valid_x):
            if previous_x == -float('inf'):
                previous_x = x
            else:
                ans = max(ans, x-previous_x)
                previous_x = x
        return ans

