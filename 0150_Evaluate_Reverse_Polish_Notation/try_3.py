class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        
        for v in tokens:
            if v == '+':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1 + n2)
            elif v == '-':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1 - n2)
            elif v == '*':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1 * n2)
            elif v == '/':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(int(n1 / n2)) # to prevent 6//-132 = -1
            else:
                stack.append(int(v))
        return stack[0]
