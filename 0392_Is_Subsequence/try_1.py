class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        if not t:
            return False
        
        index_s = 0
        
        for _t in t:
            if _t == s[index_s]:
                index_s += 1
                
                if index_s == len(s):
                    return True
        
        return False
