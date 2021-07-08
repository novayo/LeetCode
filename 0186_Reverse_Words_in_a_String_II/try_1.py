class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse s
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1
        
        # reverse word
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] != ' ':
                j += 1
            
            end = j
            j -= 1
            
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i+1, j-1
            
            i = end + 1