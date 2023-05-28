class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1

            while i < j and nums[j] % 2 == 1:
                j -= 1
            
            if i == j:
                break
            
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums
        
