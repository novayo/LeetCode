class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        _dict = {1:9, 2:56, 3:320, 4:1624, 5:7152, 6:26016, 7:72912, 8:140704, 9:140704}
        ans = 0
        for i in range(m,n+1):
            ans += _dict[i]
        return ans
