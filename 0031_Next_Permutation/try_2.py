class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        [1,2,3,4,5]
        [1,2,3,5,4]
        [1,3,2,4,5]
        
        
        # 往左找第一個小的 => a
        # 往右找下一個 略大於a的 => b
        # 交換a, b
        # reverse a+1~b-1
        '''
        
        i = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        j = i
        i -= 1
        
        if i == -1:
            nums.reverse()
            return
        
        while j < len(nums) and nums[j] > nums[i]:
            j += 1
        j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        
