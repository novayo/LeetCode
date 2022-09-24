class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        ans = i = 0
        for j in range(1, len(s)):
            if ord(s[j])-ord(s[j-1]) == 1:
                pass
            else:
                i = j
            ans = max(ans, j-i+1)
        return ans
