class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(mid):
            return nums[mid] < target
        
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid - 1
        
        return -1
