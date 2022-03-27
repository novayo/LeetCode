class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # find left
        a = b = 0
        for l in range(n):
            a += nums[l]
            b += sorted_nums[l]
            
            if a != b:
                break
        
        if a == b:
            return 0
        
        # find right
        a = b = 0
        for r in range(n-1, -1, -1):
            a += nums[r]
            b += sorted_nums[r]
            
            if a != b:
                break
        
        return r-l+1