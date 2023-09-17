class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        
        def recr(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(recr(i+1), nums[i] + recr(i+2))
            return memo[i]
        
        return recr(0)
