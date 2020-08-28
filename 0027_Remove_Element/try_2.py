class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        
        while right >= 0 and nums[right] == val:
            right -= 1
        
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                while right >= 0 and nums[right] == val:
                    right -= 1
                
            left += 1
        
        return right + 1
