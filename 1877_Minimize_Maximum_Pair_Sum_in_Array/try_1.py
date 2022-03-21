class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        i, j = 0, len(nums)-1
        
        while i < j:
            ans = max(ans, nums[j]+nums[i])
            i, j = i+1, j-1
        return ans