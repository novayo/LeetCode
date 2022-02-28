class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        l, r = 0, n-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r-l) // 2
            if nums[mid] < nums[mid+1]:
                if nums[l] < nums[mid]:
                    l = mid+1
                else:
                    r = mid
            else:
                return nums[mid+1]
        return nums[l]
