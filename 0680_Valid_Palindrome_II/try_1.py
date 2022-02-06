class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        abca
        acba
        '''
        
        n = len(s)
        reverse_s = s[::-1]
        
        for i in range(n):
            if s[:i] + s[i+1:] == reverse_s[:n-i-1] + reverse_s[n-i:]:
                return True
        return False
