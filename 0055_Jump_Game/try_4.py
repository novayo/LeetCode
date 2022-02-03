class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = ind = 0
        
        while ind < n and r >= ind:
            if ind + nums[ind] > r:
                r = ind+nums[ind]
            ind += 1
        
        return r >= n-1
