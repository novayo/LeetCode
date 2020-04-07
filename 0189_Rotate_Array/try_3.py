class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            pre = nums[-1]
            for i in range(len(nums)):
                tmp = nums[i]
                nums[i] = pre
                pre = tmp
