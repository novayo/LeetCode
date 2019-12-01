class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = globalMax = nums[0]
        for v in nums[1:]:
            localMax += v
            globalMax = max(globalMax, localMax)
            if localMax < v:
                localMax = v
                globalMax = max(globalMax, v)
        return globalMax
