class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        
        l, r = 0, len(nums)-1
        while nums[r] < nums[0]:
            if nums[r//2] < nums[0]:
                r //= 2
            else:
                break
        
        # find first peak
        while l < r:
            mid = (l+r)//2
            
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        
        if l == len(nums)-1:
            l, r = 0, l
        elif nums[0] > target:
            l, r = l+1, len(nums)-1
        else:
            l, r = 0, l

        while l < r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] == target:
                return mid
            else:
                l = mid + 1
        
        return -1 if nums[l] != target else l
