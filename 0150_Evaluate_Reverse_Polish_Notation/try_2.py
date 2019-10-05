class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        
        for v in tokens:
            if v in '+-*/':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(str(int(eval(n1+v+n2))))
            else: 
                stack.append(v)
        return stack[0]
