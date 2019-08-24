class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "O":0}
        s += "O"
        i, ans = 0, 0
        
        while s[i] != "O":
            if table[s[i]] >= table[s[i+1]]:
                ans += table[s[i]]
            else:
                ans -= table[s[i]]
            i += 1
        return ans
