class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = nums[0] 
        right = sorted(nums)
        
        for i in range(len(nums)):
            if left > right[0]:
                left = max(left, nums[i])
                right.remove(nums[i])
            else:
                break
        return max(i, 1)
