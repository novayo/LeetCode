class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Get the maximum area in a histogram given its heights
        def leetcode84(heights):
            '''
            - 邏輯 O(n)
            現在是 1 5 6
            當2近來的時候，5 6已經不會有其他可能了，所以計算完5 6之後（跟ans比對），就可以pop出來
            那再append 2即可

            最後可能會有剩下stack，因此要再計算剩下的


            - 程式邏輯
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
    
        height = len(matrix)
        width = len(matrix[0])
        
        for i in range(height):
            for j in range(width):
                matrix[i][j] = int(matrix[i][j])
        
        for i in range(height):
            for j in range(width):
                if j > 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i][j-1]
        
        ans = 0
        for j in range(width):
            ans = max(ans, leetcode84([matrix[i][j] for i in range(height)]))
        return ans