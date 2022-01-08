class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums[0:0] = [-float('inf')]
        nums.append(-float('inf'))
        
        l, r = 1, len(nums)-2
        
        while l <= r:
            mid = l + (r-l) // 2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid] <= nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        
        