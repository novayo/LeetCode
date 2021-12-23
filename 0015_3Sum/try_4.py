class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.kSum(sorted(nums), 0, 3)
    
    def kSum(self, nums, target, k):
        if len(nums) < 2 or nums[0] * k > target or nums[-1]*k < target:
            return []
        elif k == 2:
            ret = []
            found = set()
            dp = {}
            for i in range(len(nums)):
                if target - nums[i] in dp and (target-nums[i], nums[i]) not in found:
                    ret.append([target-nums[i], nums[i]])
                    found.add((target-nums[i], nums[i]))
                else:
                    dp[nums[i]] = i
            return ret
        else:
            ret = []
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]: 
                    continue
                for list in self.kSum(nums[i+1:], target-nums[i], k-1):
                    ret.append([nums[i]] + list)
            return ret
            
