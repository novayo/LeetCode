class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 掃過所有可能
        B = nums[::-1]
        ans = -float('inf')
        l = r = 1
        for i in range(len(nums)):
            if l == 0:
                l = 1
            l *= nums[i]
            
            if r == 0:
                r = 1
            r *= B[i]
            ans = max(ans, l, r)
        return ans