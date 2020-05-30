class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i*i < num:
            i += 1
        return i*i == num
