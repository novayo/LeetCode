class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [False] * n
        
        dp[0] = True
        
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if dp[j] and j+nums[j] >= i:
                    dp[i] = True
                    break
        
        return dp[n-1]
        
