class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        bigger = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = bigger
            bigger = max(bigger, tmp)
        return arr