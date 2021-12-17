class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buffer = {}
        ans = 0
        i = j = 0
        
        while j < len(s):
            if s[j] in buffer and buffer[s[j]] >= i:
                i = buffer[s[j]] + 1     
                
            buffer[s[j]] = j
            
            ans = max(ans, j-i+1)
            j += 1
        
        return ans
