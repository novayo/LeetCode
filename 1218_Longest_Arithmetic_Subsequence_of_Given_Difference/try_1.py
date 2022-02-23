class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = collections.Counter()
        ans = 0
        
        for a in arr:
            table[a] = table[a-difference] + 1
            ans = max(ans, table[a])
        
        return ans