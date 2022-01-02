class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.bisect_left(nums, target), self.bisect_right(nums, target)
    
    def bisect_left(self, nums, target):
        l, r = 0, len(nums)-1
        
        ans = float('inf')
        while l <= r:
            mid = l + (r-l) // 2
            
            if nums[mid] == target:
                ans = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans if ans != float('inf') else -1
    
    def bisect_right(self, nums, target):
        l, r = 0, len(nums) - 1
        ans = float('inf')
        
        while l <= r:
            mid = l + (r-l) // 2
            
            if nums[mid] == target:
                ans = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans if ans != float('inf') else -1
