class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        visited = set()
        ans = 0
        i = 0
        for j, _s in enumerate(s):
            while j-i >= 3 or _s in visited:
                visited.remove(s[i])
                i += 1
            
            visited.add(_s)
            
            if j-i == 2:
                ans += 1
        return ans
