class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def isFile(string):
            return '.' in string
        
        def getLevel(string):
            level = i = 0
            while i < len(string):
                if string[i] == '\t':
                    i += 1
                    level += 1
                else:
                    break
            return level
            
        
        ans = 0
        stack = []
        for filepath in input.split('\n'):
            level = getLevel(filepath)
            filepath = filepath[level:]
            
            while len(stack) > level:
                stack.pop()
            stack.append(filepath)
            
            if isFile(filepath):
                ans = max(ans, len('/'.join(stack)))
                
        return ans
