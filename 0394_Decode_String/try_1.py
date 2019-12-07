class Solution:
    def decodeString(self, s: str) -> str:
        # using stack with small stack inside
        stack = collections.deque()
        for i in s:
            if i.isnumeric():
                if len(stack) != 0 and type(stack[-1]) is int:
                    stack[-1] = stack[-1]*10 + int(i)
                else:
                    stack.append(int(i))
            elif i == "[":
                stack.append(collections.deque())
            elif i == "]":
                ss = stack.pop()
                loop = stack.pop()
                tmp = ''.join(map(str, ss))
                if len(stack) != 0 and type(stack[-1]) is collections.deque:
                    stack[-1].append(tmp*loop)
                else:
                    stack.append(tmp*loop)
            else:
                if len(stack) != 0 and type(stack[-1]) is collections.deque:
                    stack[-1].append(i)
                else:
                    stack.append(i)
        return ''.join(map(str, stack))
