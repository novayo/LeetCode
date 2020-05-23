class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                sum_i_j = abs(nums[i] + nums[j] - target)
                left = bisect.bisect_left(nums, sum_i_j - nums[-1], j+1)
                right = bisect.bisect_right(nums, sum_i_j, left)
                
                if right >= len(nums):
                    right -= 1
                
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif tmp < target:
                        left += 1
                    else:
                        right -= 1
        return list(ans)
