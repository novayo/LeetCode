class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp(index) = nums[index] + recr
        # if index >= len(nums): return 0
        
        def recr(index):
            nonlocal dp
            if index in dp:
                return dp[index]
            
            if index >= len(nums):
                dp[index] = 0
                return 0
            
            ret = 0
            for i in range(index, len(nums)):
                ret = max(ret, nums[i] + recr(i+2))
            dp[index] = ret
            return ret
        
        dp = {}
        return recr(0)
