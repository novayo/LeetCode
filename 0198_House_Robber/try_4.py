class Solution:
    def rob(self, nums: List[int]) -> int:
        idle = 0
        robbed = -float('inf')
        
        for num in nums:
            tmpIdle = idle
            idle = max(idle, robbed)
            robbed = tmpIdle + num
        
        return max(idle, robbed)