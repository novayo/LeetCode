class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        
        r = len(arr)-1
        for i in range(1, len(nums), 2):
            nums[i] = arr[r]
            r -= 1
        
        for i in range(0, len(nums), 2):
            nums[i] = arr[r]
            r -= 1
