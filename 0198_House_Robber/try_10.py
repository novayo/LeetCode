class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        no_rob, rob = 0, nums[0]
        
        for i in range(1, n):
            next_no_rob = max(no_rob, rob)
            next_rob = no_rob + nums[i]
            no_rob, rob = next_no_rob, next_rob
        
        return max(no_rob, rob)
        
        
