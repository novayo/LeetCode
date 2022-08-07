class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token in '+-*/':
                num2 = stack.pop()
                num1 = stack[-1]
                
                if token == '+':
                    stack[-1] = num1 + num2
                elif token == '-':
                    stack[-1] = num1 - num2
                elif token == '*':
                    stack[-1] = num1 * num2
                elif token == '/':
                    stack[-1] = int(num1 / num2)
            else:
                stack.append(int(token))
                
        return stack[0]
        
