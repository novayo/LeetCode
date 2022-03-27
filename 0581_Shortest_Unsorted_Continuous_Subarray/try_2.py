class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        for l in range(n):
            if sorted_nums[l] != nums[l]:
                break
        
        for r in range(n-1, -1, -1):
            if sorted_nums[r] != nums[r]:
                break
        
        if l >= r:
            return 0
        else:
            return r-l+1