class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        
        i = j = 0
        while j < len(s):
            while i < j and s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(s[j])
            ans = max(ans, j-i+1)
            j += 1
        return ans