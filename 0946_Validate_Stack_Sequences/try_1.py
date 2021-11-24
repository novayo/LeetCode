class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        loop i, j mimick stack
        '''
        stack = []
        i = j = 0
        
        while i < len(pushed):
            
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
            stack.append(pushed[i])
            i += 1
        
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        
        return len(stack) == 0
