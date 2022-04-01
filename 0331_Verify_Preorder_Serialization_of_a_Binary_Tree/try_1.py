class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True
        
        preorder = preorder.split(',')
        stack = []
        
        for i, s in enumerate(preorder):
            if s == '#':
                if not stack:
                    return False
                else:
                    while stack and stack[-1][1] == 1:
                        stack.pop()
                        
                    if stack:
                        stack[-1][1] += 1
                    elif i + 1 < len(preorder):
                        return False
            else:
                stack.append([s, 0])
        
        return len(stack) == 0