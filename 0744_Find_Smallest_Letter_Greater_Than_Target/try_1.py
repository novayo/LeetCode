class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search
        
        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left%len(letters)]
