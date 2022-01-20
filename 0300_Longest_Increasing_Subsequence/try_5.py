class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            index = bisect.bisect_left(arr, num)
            if index >= len(arr):
                arr.append(num)
            else:
                arr[index] = num
        return len(arr)
