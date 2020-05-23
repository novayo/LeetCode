class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != val:
                i += 1
            else:
                del nums[i]
        
        return len(nums)
