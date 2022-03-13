class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        ans = 0
        
        for length in range(1, len(s)+1):
            cache = set()
            for i in range(len(s)-length+1):
                target = s[i:i+length]
                if target in cache:
                    ans = length
                    break
                else:
                    cache.add(target)
        
        return ans