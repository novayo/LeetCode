class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(sorted(nums), target, 4)
    
        
    def kSum(self, nums, target, k):
        ret = []
        
        if not nums or nums[0]*k>target or nums[-1]*k<target:
            return ret
        
        if k == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for l in self.kSum(nums[i+1:], target-nums[i], k-1):
                    ret.append([nums[i]] + l)
        
        return ret
        
    
    def twoSum(self, nums, target):
        '''
        nums is a sorted list
        a + b = 0
        '''
        ret = []
        
        left, right = 0, len(nums)-1
        while left < right:
            sum = nums[left] + nums[right]
            
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                ret.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left-1] == nums[left]:
                    left += 1
        return ret