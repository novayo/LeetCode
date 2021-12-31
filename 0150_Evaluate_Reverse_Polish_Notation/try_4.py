class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def isnumeric(string):
            try:
                tmp = int(string)
                return True
            except:
                return False
        
        stack = []
        
        for token in tokens:
            if isnumeric(token):
                stack.append(token)
            else:
                string1 = stack.pop()
                string2 = stack.pop()
            
                new_string = str(int(eval(string2+token+string1)))
                stack.append(new_string)
        
        return stack[-1]
        
