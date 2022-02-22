class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        counter = collections.Counter()
        
        for i, _s in enumerate(s):
            counter[_s] += 1
            
            if max_length - max(counter.values()) < k:
                max_length += 1
            else:
                counter[s[i-max_length]] -= 1
        
        return max_length