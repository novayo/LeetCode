class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ""
        ans = ""
        for i in range(len(s)):
            ans = self.expand(ans, s, i, i)
            ans = self.expand(ans, s, i, i+1)
        return ans
    
    def expand(self, ans, s, i1, i2):
        while i1>=0 and i2<len(s) and s[i1] is s[i2]:
            i1, i2 = i1-1, i2+1
        if i2-i1-1 > len(ans):
            return s[i1+1:i2]
        else:
            return ans
        

