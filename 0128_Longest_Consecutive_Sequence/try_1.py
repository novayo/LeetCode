class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, ans = set(nums), 0
        for n in nums:
            if n-1 not in nums:
                tmp, y = 0, n
                while y in nums:
                    tmp += 1
                    y += 1
                ans = max(ans, tmp)
        return ans
