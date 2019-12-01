class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        stack = collections.deque('x')
        for v in s:
            if stack[-1] != v and stack[-1] != 'x':
                stack.pop()
                if stack[-1] == 'x':
                    ans += 1
            else:
                stack.append(v)
        return ans
