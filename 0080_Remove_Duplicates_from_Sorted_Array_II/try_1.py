class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = n = 0
        
        for j, num in enumerate(nums):
            if nums[i-1] != nums[j]:
                n = 0
                
            if n == 2 and (nums[i-1] == nums[j]):
                continue
            
            nums[i] = nums[j]
            n += 1
            i += 1
        
        return i