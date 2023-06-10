class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cache = collections.Counter()
        i = 0
        for j in range(len(s)):
            while cache[s[j]] > 0:
                cache[s[i]] -= 1
                i += 1
            
            cache[s[j]] += 1
            ans = max(ans, j-i+1)
        
        return ans