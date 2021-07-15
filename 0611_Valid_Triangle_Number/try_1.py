class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                sum = nums[i] + nums[j]
                k = bisect.bisect_left(nums, sum)
                ans += max(k-j-1, 0)
        
        return ans