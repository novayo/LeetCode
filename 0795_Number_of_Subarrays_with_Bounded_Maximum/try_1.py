class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        attempt = 0
        pre_high = -1
        for i in range(len(nums)):
            if nums[i] < left:
                ans += attempt
            
            if nums[i] > right:
                attempt = 0
                pre_high = i
            
            if left <= nums[i] <= right:
                attempt = i - pre_high
                ans += attempt
        
        return ans