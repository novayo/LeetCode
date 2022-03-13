class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack_element = []
        stack_nums = []
        
        for _s in s:
            if stack_element and stack_element[-1] == _s:
                stack_nums[-1] += 1
            else:
                stack_element.append(_s)
                stack_nums.append(1)
            
            
            while stack_nums and stack_nums[-1] == k:
                stack_element.pop()
                stack_nums.pop()
        
        
        ans = ''
        for char, num in zip(stack_element, stack_nums):
            ans += char * num
        return ans
