# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        _n = n // 2
        ans = guess(_n)
        
        while (ans):
            if ans == 1:
                _n = (_n + 1 + n) // 2
            else:
                n = _n - 1
                _n = (1 + _n) // 2
            ans = guess(_n)
            
        return _n
