class Solution:
    def firstUniqChar(self, s: str) -> int:
        found = set()
        table = {}
        
        for j in range(len(s)):
            if s[j] in found:
                table[s[j]] += len(s)
            else:
                found.add(s[j])
                table[s[j]] = j
        
        if not table:
            return -1
        tmp = min(table.values())
        if tmp < len(s):
            return tmp
        else:
            return -1
