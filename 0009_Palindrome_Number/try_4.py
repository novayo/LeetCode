class Solution:
    def isPalindrome(self, x: int) -> bool:
        def expandFromCenter(i, j):
            while i >= 0 and j < length:
                if x[i] != x[j]:
                    return False
                i, j = i-1, j+1
            return True

        x = str(x)
        length = len(x)
        mid = (length-1)//2

        if length % 2 == 0:
            return expandFromCenter(mid, mid+1)
        return expandFromCenter(mid, mid)

