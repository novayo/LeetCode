class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0] * (m+1) for _ in range(m+1)]
        
        for k in range(m-1, -1, -1):
            for i in range(k, -1, -1):
                dp[i][k] = max(
                    nums[i] * multipliers[k] + dp[i+1][k+1],
                    nums[-(k-i)-1] * multipliers[k] + dp[i][k+1]
                )
        
        return dp[0][0]
        