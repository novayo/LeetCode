class Solution:
    def calculate(self, s: str) -> int:
        '''
        先拆解文字，同時計算*/
        第二次loop: +-
        '''
        def calculate(a, symbol, b):
            if symbol == '+':
                return a+b
            elif symbol == '-':
                return a-b
            elif symbol == '*':
                return a*b
            else:
                return a//b
            
        stack = []
        n = len(s)
        cur_string = ''
        
        for i, _s in enumerate(s):
            if _s == ' ':
                continue
            elif _s in '+-*/':
                b = int(cur_string)
                if stack and stack[-1] in '*/':
                    symbol = stack.pop()
                    a = stack.pop()
                    b = calculate(a, symbol, b)
                
                stack.append(b)
                stack.append(_s)
                cur_string = ''
            else:
                cur_string += _s
        
        
        b = int(cur_string)
        if stack and stack[-1] in '*/':
            symbol = stack.pop()
            a = stack.pop()
            b = calculate(a, symbol, b)
        stack.append(b)
        
        a = stack[0]
        for i in range(1, len(stack), 2):
            a = calculate(a, stack[i], stack[i+1])
        return a