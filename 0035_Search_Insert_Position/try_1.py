class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
