class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [nums]
        count = 1
        for i in range(1, len(nums)+1):
            count *= i
        
        for i in range(count-1):
            ans.append(self.next_permutation(ans[-1]))
            
        return ans
    
    def next_permutation(self, nums):
        nums = copy.deepcopy(nums)
        i = j = len(nums) - 1
        while i >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return nums
        else:
            i -= 1
        
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        return nums
