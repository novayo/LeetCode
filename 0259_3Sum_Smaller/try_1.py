class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        return self.nSum(sorted(nums), target, 3)
        
    def nSum(self, nums, target, k):
        if not nums or nums[0]*k > target:
            return 0
        
        if k == 2:
            ret = 0
            
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] < target:
                        ret += 1
                    else:
                        break
            
            return ret
        
        ret = 0
        for i in range(len(nums)):
            ret += self.nSum(nums[i+1:], target-nums[i], k-1)
        return ret
