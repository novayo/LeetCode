class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.kSum(sorted(nums), 0, 3)
    
    def kSum(self, nums, target, k):
        if not nums or nums[-1] * k < target or nums[0] * k > target:
            return []
        
        ret = set()
        
        # two sum
        if k == 2:
            found = set()
            for num in nums:
                if target - num in found:
                    ret.add((num, target-num))
                found.add(num)
            return ret
        
        # ksum
        for i in range(len(nums)-k+1):
            if i == 0 or nums[i-1] != nums[i]:
                for _set in self.kSum(nums[i+1:], target-nums[i], k-1):
                    ret.add(tuple([nums[i]] + list(_set)))
        return ret
            
