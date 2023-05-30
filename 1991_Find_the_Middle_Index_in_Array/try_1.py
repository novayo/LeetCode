class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        for i in range(len(nums)):
            if presum[i] == presum[-1] - presum[i+1]:
                return i
        return -1
