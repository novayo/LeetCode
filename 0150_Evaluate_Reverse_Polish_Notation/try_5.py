class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                stack.append(str(int(eval(a + token + b))))
            else:
                stack.append(token)
        return int(stack[0])
