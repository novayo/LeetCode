class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(i, j):
            while i >= 0 and j < length:
                if s[i] != s[j]:
                    break
                i, j = i-1, j+1
            
            return s[i+1: j]
            
        
        ans = ""
        length = len(s)
        for i in range(length):
            result = expandFromCenter(i, i)
            if len(result) > len(ans):
                ans = result
            
            if i + 1 < length and s[i] == s[i+1]:
                result = expandFromCenter(i, i+1)
                if len(result) > len(ans):
                    ans = result
        
        return ans

