class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        prefix_max = [-float('inf')] * n
        cur_max = height[0]
        for i in range(1, n):
            prefix_max[i] = cur_max
            cur_max = max(cur_max, height[i])
        
        
        suffix_max = [-float('inf')] * n
        cur_max = height[-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = cur_max
            cur_max = max(cur_max, height[i])
        
        ans = 0
        for i in range(n):
            _min = min(prefix_max[i], suffix_max[i])
            ans += max(_min - height[i], 0)
        return ans
            
