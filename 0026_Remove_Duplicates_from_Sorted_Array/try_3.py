class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        curNum = float('inf')
        i = 0
        for j in range(len(nums)):
            if nums[j] != curNum:
                curNum = nums[j]
                nums[i] = nums[j]
                i += 1
        return i
