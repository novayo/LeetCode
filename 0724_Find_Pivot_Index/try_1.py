class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = right = 0
        
        for num in nums:
            right += num
        
        for i in range(len(nums)):
            if i > 0:
                left += nums[i-1]
            right -= nums[i]
            
            if left == right:
                return i
        
        return -1
