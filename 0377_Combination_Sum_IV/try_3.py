class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1
        
        for t in range(1, target+1):
            for num in nums:
                if target-num >= 0:
                    dp[t] += dp[t-num]
        return dp[target]