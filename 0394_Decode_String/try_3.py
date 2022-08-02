class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []
        for i, _s in enumerate(s):
            if _s == '[':
                stack.append(i)
            elif _s == ']':
                pair[stack.pop()] = i
        
        
        def getString(i, j):
            ret = cur = ''
            while i <= j:
                if s[i].isdigit():
                    cur += s[i]
                elif s[i] == '[':
                    ret += int(cur) * getString(i+1, pair[i]-1)
                    i = pair[i]
                    cur = ''
                else:
                    ret += s[i]
                
                i += 1
            return ret
        
        return getString(0, n-1)