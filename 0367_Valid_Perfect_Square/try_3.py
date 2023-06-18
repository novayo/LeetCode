class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 1, num
        while i <= j:
            mid = i + (j-i) // 2
            result = mid * mid
            if result == num:
                return True
            elif result < num:
                i = mid + 1
            else:
                j = mid - 1
        return False