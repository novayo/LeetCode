class Solution:
    def trap(self, height: List[int]) -> int:
        # mononic stack
        
        ans = 0
        stack = [] # (index)
        
        for i in range(len(height)):
            target = height[i]
            
            while stack and height[stack[-1]] <= target:
                bot = stack.pop()
                ans += (min(height[stack[-1]], target) - height[bot]) * (i - stack[-1] - 1) if stack else 0
            stack.append(i)
        
        return ans
