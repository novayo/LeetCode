class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_peak(nums):
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l+r) // 2
                if nums[mid] < nums[l]:
                    r = mid
                elif nums[mid] < nums[mid+1]:
                    l = mid+1
                else:
                    r = mid
            return l
        
        peak = find_peak(nums)
        
        if nums[0] <= target:
            index = bisect.bisect_left(nums[:peak+1], target)
        else:
            index = bisect.bisect_left(nums[peak+1:], target) + peak + 1
        
        return -1 if index >= len(nums) or nums[index] != target else index
