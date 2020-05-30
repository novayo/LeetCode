class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l<r:
            mid = (l+r)//2
        
            if r-l == 2:
                if nums[l] == nums[mid]:
                    return nums[r]
                else:
                    return nums[l]
            elif mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    l = mid
                elif nums[mid] == nums[mid-1]:
                    r = mid
                else:
                    return nums[mid]
            elif mid % 2 == 1:
                if nums[mid] == nums[mid+1]:
                    r = mid
                elif nums[mid] == nums[mid-1]:
                    l = mid+1
                else:
                    return nums[mid]
            
        return nums[l]
