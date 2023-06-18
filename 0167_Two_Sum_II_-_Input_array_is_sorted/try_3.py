class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            j = self.bisect_left(numbers, target-num, i+1)
            if j < len(numbers) and num + numbers[j] == target:
                return [i+1, j+1]
    
    def bisect_left(self, arr, target, startIdx):
        ans = -1
        i = startIdx
        j = len(arr)-1
        while i <= j:
            mid = i + (j-i) // 2
            if arr[mid] < target:
                i = mid+1
            elif arr[mid] > target:
                j = mid-1
            else:
                ans = mid
                j = mid-1
        return ans if ans != -1 else i