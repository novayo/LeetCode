class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for cur in range(1, target+1):
            for coin in nums:
                if cur - coin >= 0:
                    dp[cur] += dp[cur-coin]
        
        return dp[target]