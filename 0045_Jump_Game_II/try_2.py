class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        從尾巴算回來，去最小的每種可能性即可
        '''
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        
        for i in range(len(nums)-1, -1, -1):
            target = nums[i]
            
            for j in range(target):
                index = i + j + 1
                if index >= len(nums):
                    break
                dp[i] = min(dp[i], 1+dp[index])
        
        return dp[0]
