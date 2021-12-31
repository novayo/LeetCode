class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # LCS
        
        arr = []
        for num in nums:
            index = bisect.bisect_left(arr, num)
            if index >= len(arr):
                arr.append(num)
                if len(arr) >= 3:
                    return True
            else:
                arr[index] = num
        
        return len(arr) >= 3
