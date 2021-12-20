class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        '''
        2ax+b = 0
        x = -b/2a
        '''
        if a == 0:
            nums = [b*nums[i] + c for i in range(len(nums))]
            return nums if b > 0 else nums[::-1]
        
        
        middle_x = -b/(2*a)
        
        if a > 0:
            r = bisect.bisect_right(nums, middle_x)
            l = r - 1
        else:
            r, l = 0, len(nums)-1
        
        ans = [0] * len(nums)
        i = 0
        while i < len(ans) and (l >= 0 or r < len(nums)):
            left = right = float('inf')
            
            if l >= 0:
                left = a*(nums[l]**2) + b*(nums[l]) + c
            if r < len(nums):
                right = a*(nums[r]**2) + b*(nums[r]) + c
            
            if left <= right:
                ans[i] = left
                l -= 1
            else:
                ans[i] = right
                r += 1
            
            i += 1
        
        return ans
            
