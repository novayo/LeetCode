class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums.sort()
        
        ans = 0
        j = len(nums)-1
        for i in range(len(nums)):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            
            if i > j:
                break
            
            if nums[i] + nums[j] <= target:
                ans = (ans + pow(2, (j-i) , MOD)) % MOD
        return ans