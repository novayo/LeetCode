class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        
        subset_target = s // k
        nums.sort()
        if nums[-1] > subset_target:
            return False
        
        
        while nums and nums[-1] == subset_target:
            nums.pop()
            k -= 1
        
        def helper(parts, index):
            if index < 0:
                return True
            
            for i in range(k):
                parts[i] += nums[index]
                if parts[i] <= subset_target:
                    if helper(parts, index-1):
                        return True
                parts[i] -= nums[index]
                if parts[i] == 0:
                    break
            return False
        
        return helper([0] * k, len(nums)-1)
