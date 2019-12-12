# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Ternary search
        
        low, high = 1, n
        while low <= high:
            mid1 = low + (high - low) // 3  # (int)(high / 3 + (2 * low) / 3)
            mid2 = high - (high - low) // 3 #(int)((2 * high) / 3 + low / 3)
            res1 = guess(mid1)
            res2 = guess(mid2)
            
            if res1 == 0:
                return mid1
            elif res2 == 0:
                return mid2
            elif res1 == -1:
                high = mid1 - 1
            elif res2 == 1:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        return  -1
