class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i, ans, delta = 0, "", 1 if numRows is 1 else 2 * numRows - 2
        while i < len(s):
            ans += s[i]
            i += delta
    
        for j in range(1, numRows):
            i, k = j, 2 * j
            while i < len(s):
                ans += s[i]
                k = delta if (k == delta) else (delta - k)
                i += k
        
        return ans
