class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur_max = nums[0]
        for num in nums[1:]:
            cur_max = max(num, num + cur_max)
            ans = max(ans, cur_max)
        return ans
