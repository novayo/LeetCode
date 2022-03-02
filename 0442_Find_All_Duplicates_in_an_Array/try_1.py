class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            nums[abs(num)-1] *= -1
        return ans