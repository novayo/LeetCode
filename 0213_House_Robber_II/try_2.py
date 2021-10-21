class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def house_robber(nums, _min = False):
            if not nums:
                return 0
            func = min if _min else max 
            
            ans = func(nums[:2])
            cur_max = nums[0]
            dp = copy.copy(nums)
            
            for i in range(2, len(dp)):
                dp[i] += cur_max
                cur_max = func(cur_max, dp[i-1])
                ans = func(ans, dp[i])
            
            return ans
        
        index_0_to_neg2 = house_robber(nums[:-1])
        index_1_to_neg1 = house_robber(nums[1:])
        
        return max(index_0_to_neg2, index_1_to_neg1)
