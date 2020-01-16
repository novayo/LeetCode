class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]: # Finding first decreasing element (a[i])
            i -= 1
        
        if i == 0: # Nums are in descending order
            nums.reverse()
            return
        else: # Decreasing element found
            i -= 1
        
        while j >= 0 and nums[i] >= nums[j]: # Finding element just larger than a[i-1] (a[j])
            j -= 1
            
        nums[i], nums[j] = nums[j], nums[i] # Swap(a[i-1], a[j])
        nums[i+1:] = reversed(nums[i+1:]) # Reverse a[i+1:]
