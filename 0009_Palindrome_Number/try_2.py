class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)

        i, j = 0, length-1
        while i <= j:
            if x[i] != x[j]:
                return False
            
            i, j = i+1, j-1
        return True
