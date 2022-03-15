class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = l = 0
        r = len(nums)-1
        
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i = max(l, i)
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
        