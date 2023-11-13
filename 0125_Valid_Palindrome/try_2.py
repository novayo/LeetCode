class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(char):
            ascii = ord(char.lower())
            return 97 <= ascii <= 122 or 48 <= ascii <= 57

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not isAlphanumeric(s[i]):
                i += 1
            
            while i < j and not isAlphanumeric(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            
            i, j = i+1, j-1
        
        return True
