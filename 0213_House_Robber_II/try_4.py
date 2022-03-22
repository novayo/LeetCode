class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        return max(
            self.house_robber(nums[:-1]),
            self.house_robber(nums[1:])
        )
    
    def house_robber(self, nums):
        if len(nums) <= 2:
            return max(nums)
        
        a, b = nums[0], nums[1]
        c = a + nums[2]
        
        for i in range(3, len(nums)):
            d = nums[i] + max(a,  b)
            a = b
            b = c
            c = d
        
        return max(b, c)