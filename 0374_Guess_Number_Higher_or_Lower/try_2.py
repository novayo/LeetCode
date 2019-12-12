# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search
        low, high = 1, n
        while (low <= high):
            mid = (low + high) // 2
            res = guess(mid)
            if (res == 0):
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
        return -1
