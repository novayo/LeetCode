class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def getLevel(string):
            level = 1
            for i in range(0, len(string)):
                if string[i:i+1] == '\t':
                    level += 1
                else:
                    break
            return level, string[level-1:]
        
        def isFile(string):
            return '.' in s
        
        ans = 0
        cur_length = 0
        stack = []
        for string in input.split('\n'):
            level, s = getLevel(string)
            
            while level <= len(stack):
                cur_length -= len(stack.pop())
            
            if isFile(s):
                ans = max(ans, cur_length + len(stack) + len(s))
            else:
                cur_length += len(s)
                stack.append(s)
        return ans
                
            
            
