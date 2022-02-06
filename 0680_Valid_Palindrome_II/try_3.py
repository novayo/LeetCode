class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        
        n = len(s)
        i, j = 0, n-1
        
        while i < j:
            if s[i] == s[j]:
                i, j = i+1, j-1
            else:
                # left
                if s[i+1: j+1] == s[i+1: j+1][::-1] or \
                   s[i: j] == s[i: j][::-1]:
                    return True
                else:
                    return False
        return True
