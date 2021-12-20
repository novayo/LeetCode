class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        while n > digit*9*(10**(digit-1)):
            n -= digit*9*(10**(digit-1))
            digit += 1
        
        return str(10**(digit-1) + (n-1) //digit)[n % digit - 1]

