class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find peak
        nums[0:0] = [-float('inf')]
        nums.append(-float('inf'))
        
        l, r = 1, len(nums)-2
        while l <= r:
            mid = l + (r-l) // 2
            
            if nums[1] > nums[mid]:
                r = mid - 1
            elif nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                l = mid
                break
            elif nums[mid] <= nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        
        peak_index = l
        
        
        # search left or right
        offset = 0
        if nums[1] <= target <= nums[peak_index]:
            l, r = 1, peak_index
        else:
            l, r = peak_index+1, len(nums)-2
        
        # binary search left
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid-1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
        
