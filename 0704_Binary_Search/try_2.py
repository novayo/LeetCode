class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        ans = -float('inf')
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                ans = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return ans if ans > -float('inf') else -1
        
