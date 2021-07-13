class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def condition(index):
            return nums[index+1] > nums[index]
        
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = (l+r) // 2
            if condition(mid):
                l = mid+1
            else:
                r = mid
        
        return l