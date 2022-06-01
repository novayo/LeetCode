class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = []
        suffix = [0] * n
        
        prefix.append(nums[0])
        for num in nums[1:]:
            prefix.append(min(prefix[-1], num))
        
        suffix.append(nums[-1])
        for num in nums[::-1][1:]:
            suffix.append(max(suffix[-1], num))
        suffix.reverse()
        
        ans = l = r = 0
        while r < n:
            if prefix[l] <= suffix[r]:
                ans = max(ans, r-l)
                r += 1
            else:
                l += 1
        return ans