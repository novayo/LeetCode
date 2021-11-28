class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        if len(s) < k:
            return len(s)
        
        index_table = {}
        i = j = ans = 0
        
        while j < len(s):
            index_table[s[j]] = j
            j += 1
            
            if len(index_table) > k:
                _min = min(index_table.values())
                del index_table[s[_min]]
                i = _min + 1
                
            ans = max(ans, j-i)
        return ans