class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        
        for i, num in enumerate(nums):
            farest = max(farest, i + num)

            if farest == len(nums)-1:
                break
            if farest == i:
                return False
        
        return True