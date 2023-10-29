class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        _sum = sum(nums)
        
        if _sum % 2 == 1:
            return False
        
        target = _sum // 2
        
        @lru_cache(None)
        def recr(i, cur_sum):
            if cur_sum == target:
                return True
            if i >= n:
                return False
            
            return recr(i+1, cur_sum) or recr(i+1, cur_sum + nums[i])
        
        return recr(0, 0)
