class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        i, j = 0, n-1
        while i <= j:
            mid = i + (j-i) // 2
            
            if mid+1 < n and nums[mid] <= nums[mid+1]:
                i = mid + 1
            else:
                ans = mid
                j = mid - 1
        
        return ans
            