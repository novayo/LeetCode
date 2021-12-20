class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        dp = [False] * len(s)
        
        # mark
        for word in words:
            i = j = 0
            while len(s)-i >= len(word):
                j = i
                while j-i < len(word) and j < len(s) and s[j] == word[j-i]:
                    j += 1
                
                if j-i == len(word):
                    dp[i:j] = [True] * len(word)
                
                i += 1
        
        # get ans
        i = j = len(s)-1
        while i >= 0:
            j = i
            if dp[i] == True:
                while i >= 0 and dp[i] == True:
                    i -= 1
                s = s[:i+1] + '<b>' + s[i+1:j+1] + '</b>' + s[j+1:]
            else:
                i -= 1
        return s
        
