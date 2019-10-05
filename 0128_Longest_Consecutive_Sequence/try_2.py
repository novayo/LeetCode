class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, ans = set(nums), 0
        for n in nums:
            if n-1 not in nums:
                y = n+1
                while y in nums:
                    y += 1
                ans = max(ans, y-n)
        return ans
