class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        
        ans = 0
        cur_max = nums[-1][1]
        
        for _, i in nums[::-1]:
            ans = max(ans, cur_max-i)
            cur_max = max(cur_max, i)
        return ans