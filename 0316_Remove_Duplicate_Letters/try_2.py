class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        
        last_index = {}
        for i in range(n-1, -1, -1):
            if s[i] in last_index:
                continue
            last_index[s[i]] = i
        
        
        stack = []
        in_stack = set()
        
        for i, _s in enumerate(s):
            if _s in in_stack:
                continue
            
            while stack and stack[-1] > _s and i < last_index[stack[-1]]:
                in_stack.remove(stack[-1])
                stack.pop()
            
            stack.append(_s)
            in_stack.add(_s)
            
        return ''.join(stack)
