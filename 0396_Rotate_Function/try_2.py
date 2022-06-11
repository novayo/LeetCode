class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sumA = sum(nums)
        
        # init
        cur = 0
        for i, num in enumerate(nums):
            cur += i * num
        
        
        # get max ans
        ans = cur
        for i in range(n-1):
            cur += sumA - n * nums[~i]
            ans = max(ans, cur)
        return ans