class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum % k != 0:
            return False
        
        target = _sum // k
        nums.sort()
        if nums[-1] > target:
            return False
        while len(nums) > 0 and nums[-1] == target:
            nums.pop()
            k -= 1
        
        return self.helper([0] * k, nums, target)
    
    def helper(self, parts, nums, target):
        if len(nums) == 0:
            return True
        selectedNumber = nums.pop()
        
        for i, v in enumerate(parts):
            if selectedNumber + v <= target:
                parts[i] += selectedNumber
                if self.helper(parts, nums, target):
                    return True
                parts[i] -= selectedNumber
            
            if parts[i] == 0:
                break
        
        nums.append(selectedNumber)
        return False
