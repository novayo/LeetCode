class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)

        max_length = 0
        has_odd = False
        for key, count in counter.items():
            if count % 2 == 0:
                max_length += count
            else:
                if count > 1:
                    max_length += count - 1
                has_odd = True
        
        if has_odd:
            max_length += 1
        return max_length
            
