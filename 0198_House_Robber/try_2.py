class Solution:
    def rob(self, nums: List[int]) -> int:
        # button-up
        nums += [0,0]
        dp = [0]*(len(nums))
        for i in range(len(nums)-1, -1, -1):
            for j in range(2, len(nums)-i):
                dp[i] = max(dp[i], nums[i] + dp[i+j])
        return max(dp[0], dp[1])
