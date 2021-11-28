class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        index_table = {}
        i = j = ans = 0
        
        while j < len(s):
            index_table[s[j]] = j
            
            if len(index_table) > 2:
                ans = max(ans, j-i)
                _min = min(index_table.values())
                del index_table[s[_min]]
                i = _min + 1
                
            j += 1
        
        ans = max(ans, j-i)
        return ans