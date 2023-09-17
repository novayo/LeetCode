class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        
        def recr(i):
            if i >= n-1:
                return True
            elif nums[i] == 0:
                return False
            
            if i in memo:
                return memo[i]
            
            for dist in range(nums[i], 0, -1):
                memo[i] = recr(i + dist)
                if memo[i]:
                    return memo[i]
            return False
        
        return recr(0)
