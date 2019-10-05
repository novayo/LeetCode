class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if not num else 1+(num-1)%9
