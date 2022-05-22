class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        table = {}
        found = set()
        def dfs(p, i):
            if p >= len(pattern) and i >= len(s):
                return True
            elif p >= len(pattern):
                return False
            elif i >= len(s):
                return False
            
            if pattern[p] in table:
                pat = table[pattern[p]]
                if s[i:i+len(pat)] == pat:
                    if dfs(p+1, i+len(pat)):
                        return True
                
                return False
            
            for j in range(i, len(s)):
                pat = s[i:j+1]
                
                if pat in found:
                    continue
                
                found.add(pat)
                table[pattern[p]] = pat
                if dfs(p+1, j+1):
                    return True
                del table[pattern[p]]
                found.remove(pat)
            return False
        
        return dfs(0, 0)
                
