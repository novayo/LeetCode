class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hash table
        if len(s) != len(t):
            return False
        
        sTable = {}
        tTable = {}
        
        for i in range(len(s)):
            if s[i] in sTable:
                if sTable[s[i]] != t[i]:
                    return False
            else:
                sTable[s[i]] = t[i]
            
            if t[i] in tTable:
                if tTable[t[i]] != s[i]:
                    return False
            else:
                tTable[t[i]] = s[i]
        
        return True