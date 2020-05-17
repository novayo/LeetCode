class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == ')':
                stack.pop()
                if stack:
                    ans = max(ans, i-stack[-1])
                else:
                    stack.append(i)    
            else:
                stack.append(i)
        return ans
