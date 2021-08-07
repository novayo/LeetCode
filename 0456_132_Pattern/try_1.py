class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        _min = float('inf')
        for i in range(len(nums)-1):
            _min = min(_min, nums[i])
            for j in range(i+1, len(nums)):
                if _min < nums[j] < nums[i]:
                    return True
        return False
