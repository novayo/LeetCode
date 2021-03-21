class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        monotonic stack: push index
        '''
        ans = 0
        index = 0
        stack = []
        
        while index < len(height):
            if len(stack) == 0 or height[stack[-1]] > height[index]:
                stack.append(index)
                index += 1
            else:
                bottom = stack.pop()
                
                # 沒有左牆壁的情況
                if len(stack) == 0:
                    continue
                
                # 計算高
                calculate_height = min(height[stack[-1]], height[index]) - height[bottom]
                
                # 計算寬
                width = index - stack[-1] - 1
                ans += calculate_height * width
        return ans
