class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        ans, i, _max = 0, 0, height.index(max(height))
        for element in range(_max):
            j = height[element]
            if i <= j:
                i = j
            else:
                ans += i-j
        
        i = 0
        for element in range(len(height)-1, _max, -1):
            j = height[element]
            if i <= j:
                i = j
            else:
                ans += i-j
        
        return ans
