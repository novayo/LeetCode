class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        lower = float('inf')
        for i in range(n-3, -1, -1):
            if i+2 < n:
                lower = min(lower, nums[i+2])
            if nums[i] > lower:
                return False
        return True
