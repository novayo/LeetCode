class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            right_most_x = x & 1
            right_most_y = y & 1
            
            if right_most_x != right_most_y:
                ans += 1
            
            x = x >> 1
            y = y >> 1
            
        return ans
            
