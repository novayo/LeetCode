class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            ans = -float('inf')
            cur_sum = 0
            for num in nums:
                cur_sum += num
                ans = max(ans, cur_sum)
                
                if cur_sum < 0:
                    cur_sum = 0
            return ans
        
        
        return max(
            kadane(nums),
            sum(nums) + kadane([-num for num in nums[:-1]]),
            sum(nums) + kadane([-num for num in nums[1:]])
        )