class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        a, b, c = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, len(nums)):
            d = nums[i] + max(a, b)
            a, b, c = b, c, d
        return max(a, b, c)
        
