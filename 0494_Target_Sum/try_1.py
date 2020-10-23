class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = {}
        def dfs(index, sum, count, dp):
            if (index, sum, count) in dp:
                return dp[index, sum, count]
            
            if index == len(nums):
                dp[index, sum, count] = 1 if sum == S else 0
                return dp[index, sum, count]
            
            dp[index, sum, count] = dfs(index+1, sum+nums[index], count+1, dp) + dfs(index+1, sum-nums[index], count+1, dp)
            return dp[index, sum, count]
        
        return dfs(0, 0, 0, dp)