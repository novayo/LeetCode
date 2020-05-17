class Solution:
    def maxPower(self, s: str) -> int:
        w = s[0]
        ans = 1
        tmp = 1
        for i in s[1:]:
            if w == i:
                tmp += 1
                ans = max(ans, tmp)
            else:
                w = i
                tmp = 1
        return ans
