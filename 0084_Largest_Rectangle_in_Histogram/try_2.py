class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        stack 放入 index
        for loop 0~len(heights)
            比top大，就放進去
            比top小，就pop到比top大，且去計算答案：heights[stack[top]] * (i - stack[top] - 1)
        
        若stack還有東西要pop到比top大，且去計算答案：heights[stack[top]] * (i - stack[top] - 1)
        
        回傳 ans
        '''
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
