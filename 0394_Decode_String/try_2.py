class Solution:
    def decodeString(self, s: str) -> str:
        '''
        stack
        '''
        def isInt(s):
            if "0" <= s <= "9":
                return True
            else:
                return False
        
        stack = []
        
        for _s in s:
            if _s == ']':
                # get string
                tmp_s = ''
                while stack and stack[-1] != '[':
                    tmp_s = stack.pop() + tmp_s
                
                # pop [
                stack.pop()
                
                # get number
                tmp_i = ''
                while stack and len(stack[-1]) == 1 and isInt(stack[-1]):
                    tmp_i = stack.pop() + tmp_i
                tmp_i = int(tmp_i)
                
                # push ans in stack
                stack.append(tmp_s * tmp_i)
            else:
                stack.append(_s)
        
        return ''.join(stack)
