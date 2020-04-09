class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums.sort()
        found = set()
        t = tuple(nums)
        
        while t not in found:
            i = len(nums)-1
            while i>0 and nums[i-1] >= nums[i]:
                i-=1

            i = j = i - 1
            while j<len(nums)-1 and nums[i] < nums[j+1]:
                j += 1

            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
            
            found.add(t)
            t = tuple(nums)
        
        return list(found)
