class Solution:
    def rob(self, nums: List[int]) -> int:
        cur_max = nums[0]
        
        for i in range(2, len(nums)):
            cur_max = max(cur_max, nums[i-2])
            nums[i] += cur_max
        
        return max(nums[-2:])
