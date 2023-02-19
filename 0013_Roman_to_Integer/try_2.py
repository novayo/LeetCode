class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rank_map = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
        
        i = ans = 0
        while i < n:
            if i+1 < n and rank_map[s[i]] < rank_map[s[i+1]]:
                ans += value_map[s[i+1]] - value_map[s[i]]
                i += 2
            else:
                ans += value_map[s[i]]
                i += 1
        return ans

