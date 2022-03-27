class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        
        
        min_stack = []
        for i in range(2*n):
            num = nums[i%n]
            
            while min_stack and min_stack[-1][0] < num:
                value, index = min_stack.pop()
                ans[index] = num
            
            if ans[i%n] == -1:
                min_stack.append([num, i%n])
        return ans
        