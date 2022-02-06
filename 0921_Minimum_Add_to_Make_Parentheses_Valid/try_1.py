class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for _s in s:
            if stack and _s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(_s)
        return len(stack)

