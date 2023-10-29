class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        _sum = sum(nums)
        
        if _sum % 2 == 1:
            return False
        
        dp = [False] * (_sum+1)
        dp[0] = True
        
        for num in nums:
            for i in range(_sum, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        target = _sum // 2
        return dp[target]
