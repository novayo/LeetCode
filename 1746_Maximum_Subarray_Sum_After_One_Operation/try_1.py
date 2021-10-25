class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[-float('inf')] * 2 for i in range(len(nums))]
        
        dp[0][0] = nums[0]
        dp[0][1] = nums[0] ** 2
        
        ans = max(dp[0][0], dp[0][1])
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0] + nums[i], nums[i])
            dp[i][1] = max(dp[i-1][0] + nums[i] ** 2, dp[i-1][1] + nums[i], nums[i] ** 2)
            ans = max(ans, dp[i][0], dp[i][1])
        return ans
