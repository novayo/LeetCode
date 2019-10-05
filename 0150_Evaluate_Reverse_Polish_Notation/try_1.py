class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def checkStack():
            nonlocal stack
            for i in range(len(stack)-2):
                if len(stack)<3: return
                if not stack[-3].isdigit() and bool(re.match('[-]?[0-9]+', stack[-1])) and bool(re.match('[-]?[0-9]+', stack[-2])):
                    n1 = stack.pop()
                    n2 = stack.pop()
                    op = stack.pop()
                    
                    if op == '+':
                        stack.append(str(int(n1)+int(n2)))
                    elif op == '-':
                        stack.append(str(int(n1)-int(n2)))
                    elif op == '*':
                        stack.append(str(int(n1)*int(n2)))
                    elif op == '/':
                        stack.append(str(int(int(n1)/int(n2))))
                else:
                    return
        
        stack = collections.deque()
        for v in tokens[::-1]:
            stack.append(v)
            checkStack()
            
        return stack[-1]
