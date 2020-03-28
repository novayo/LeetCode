class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        
        ans = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                peek = stack.pop()
                ans = max(ans, heights[peek] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            peek = stack.pop()
            ans = max(ans, heights[peek] * (len(heights) - stack[-1] - 1))
        
        return ans
