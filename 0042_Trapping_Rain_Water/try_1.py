class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        _maxIndex = height.index(max(height))
        tmp, ans = 0, 0
        
        for i in range(_maxIndex):
            if height[i] > tmp:
                tmp = height[i]
            elif height[i] < tmp:
                ans += tmp-height[i]
        
        tmp = 0
        for i in range(len(height)-1, _maxIndex, -1):
            if height[i] > tmp:
                tmp = height[i]
            elif height[i] < tmp:
                ans += tmp-height[i]
        return ans
