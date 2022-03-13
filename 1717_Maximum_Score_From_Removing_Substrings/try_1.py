class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy        
        a, b = 'ab', 'ba'
        if x < y:
            x, y = y, x
            a, b = b, a
        
        
        ans = 0
        stack = []
        for _s in s + '#':
            if stack and stack[-1] + _s == a:
                stack.pop()
                ans += x
            else:
                stack.append(_s)
        
        s = ''.join(stack)
        
        stack = []
        for _s in s + '#':
            if stack and stack[-1] + _s == b:
                stack.pop()
                ans += y
            else:
                stack.append(_s)
        
        return ans
