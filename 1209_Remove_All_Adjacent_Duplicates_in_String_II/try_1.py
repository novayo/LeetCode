class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Using stack
        stack = [["#", 0]]
        
        for value in s:
            if stack[-1][0] == value:
                stack[-1][1] += 1
            else:
                stack.append([value, 1])
            while stack[-1][1] >= k:
                stack.pop()
        return "".join(i*j for i, j in stack)
