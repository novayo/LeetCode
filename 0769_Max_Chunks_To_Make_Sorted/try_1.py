class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = sorted_sum = current_sum = 0
        
        for i, a in enumerate(arr):
            sorted_sum += i
            current_sum += a
            
            if sorted_sum == current_sum:
                ans += 1
                sorted_sum = current_sum = 0
        
        return ans
