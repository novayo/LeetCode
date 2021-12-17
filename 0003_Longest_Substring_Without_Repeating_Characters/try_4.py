class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buffer = {}
        ans = 0
        i = j = 0
        
        while j < len(s):
            if s[j] in buffer:
                # maintain previous buffer
                while i < buffer[s[j]]:
                    del buffer[s[i]]
                    i += 1
                i += 1       
                
            buffer[s[j]] = j
            
            ans = max(ans, j-i+1)
            j += 1
        
        return ans
