class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = lastPos = len(nums) - 1
        while i>=0:
            if i + nums[i] >= lastPos:
                lastPos = i
            i -= 1
        
        return lastPos == 0
