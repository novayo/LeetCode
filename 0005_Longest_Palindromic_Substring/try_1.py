class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        def expandFromMiddle(i, j):
            while i > 0 and j < len(s)-1:
                if s[i-1] == s[j+1]:
                    i -= 1
                    j += 1
                else:
                    break
            return i, j+1
        
        ans = ""
        for index in range(len(s)-1):
            tmp = expandFromMiddle(index, index)
            if tmp[1]-tmp[0] > len(ans):
                ans = s[tmp[0]:tmp[1]]
            
            if s[index] == s[index+1]:
                tmp = expandFromMiddle(index, index+1)
                if tmp[1]-tmp[0] > len(ans):
                    ans = s[tmp[0]:tmp[1]]
        
        return ans
