class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        counter = collections.Counter()
        ans = 0
        
        for val in arr:
            counter[val] = counter[val - difference] + 1
            ans = max(ans, counter[val])
        
        return ans
        
