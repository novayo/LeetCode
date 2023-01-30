class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_right(nums, target-1)
        
        if index >= len(nums) or nums[index] != target:
            return -1
        return index

