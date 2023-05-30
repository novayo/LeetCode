class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min = float('inf')
        presum = 0
        for num in nums:
            presum += num
            _min = min(_min, presum)
        return max(-_min + 1, 1)

