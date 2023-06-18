class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]

        n = len(nums)
        i, j = 0, n-1
        while i <= j:
            mid = i + (j-i) // 2
            
            # If found the answer
            if (mid+1 == n or nums[mid] != nums[mid+1]) and (mid == 0 or nums[mid] != nums[mid-1]):
                return nums[mid]
            
            if mid % 2 == 0:
                if mid < n and nums[mid] == nums[mid+1]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if mid > 0 and nums[mid] == nums[mid-1]:
                    i = mid + 1
                else:
                    j = mid - 1
        
        return -1