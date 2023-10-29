class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        
        for val in range(target+1):
            for num in nums:
                if val < num:
                    continue
                
                dp[val] += dp[val - num]
        
        return dp[target]
        
