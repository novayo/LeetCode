class Solution:
    def decodeString(self, s: str) -> str:
        pair = {}
        stack = []
        for i, _s in enumerate(s):
            if _s == '[':
                stack.append(i)
            elif _s == ']':
                pair[stack.pop()] = i
        
        
        def recr(i, j):
            ret = ''
            cur_int = ''
            while i <= j:
                if s[i].isdigit():
                    cur_int += s[i]
                elif s[i] == '[':
                    ret += int(cur_int) * recr(i+1, pair[i]-1)
                    cur_int = ''
                    i = pair[i]
                else:
                    ret += s[i]
                
                i += 1
            
            return ret
        
        return recr(0, len(s)-1)
