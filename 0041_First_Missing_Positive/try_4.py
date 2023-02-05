class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # O(n): mark found element
        MARKED = "T"
        for i, v in enumerate(nums):
            while v != MARKED and 0 < v <= n:
                temp = nums[v-1]
                nums[v-1] = MARKED
                v = temp
        
        # O(n): get ans
        for i in range(n):
            if nums[i] != MARKED:
                return i+1
        return n+1
