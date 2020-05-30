class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "0P":
            return False
        i = 0
        j = len(s)-1
        
        alpha = set()
        for k in range(10):
            alpha.add(48+k)
        
        for k in range(26):
            alpha.add(65+k)
            alpha.add(97+k)
        
        while i<=j:
            ascii_i = ord(s[i])
            ascii_j = ord(s[j])

            if ascii_i not in alpha:
                i += 1
            elif ascii_j not in alpha:
                j -= 1
            elif ascii_i == ascii_j or abs(ascii_i-ascii_j) == 32:
                i += 1
                j -= 1
            else:
                return False
            
        return True
