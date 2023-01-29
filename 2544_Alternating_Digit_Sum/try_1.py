class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        pos = True
        for _s in str(n):
            if pos:
                ans += int(_s)
            else:
                ans -= int(_s)
            pos = not pos
        return ans

