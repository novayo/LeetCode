class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        固定一個轉成3sum
        '''
        nums.sort()
        
        ret = set()
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for l in self.threeSum(nums, target - nums[i], i+1):
                    ret.add(tuple([nums[i]] + l))
        return list(ret)
        
    def threeSum(self, nums, target, index):
        ret = []
        
        for i in range(index, len(nums)):
            left, right = i+1, len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return ret