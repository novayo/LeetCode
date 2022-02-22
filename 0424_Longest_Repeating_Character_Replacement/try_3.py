class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = max_counter = 0
        counter = collections.Counter()
        
        for i, _s in enumerate(s):
            counter[_s] += 1
            
            max_counter = max(max_counter, counter[_s])
            if max_length - max_counter < k:
                max_length += 1
            else:
                counter[s[i-max_length]] -= 1
        
        return max_length