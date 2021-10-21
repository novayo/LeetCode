class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        ans = -float('inf')
        cur_min = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i] - cur_min)
            cur_min = min(cur_min, nums[i])
        return ans
