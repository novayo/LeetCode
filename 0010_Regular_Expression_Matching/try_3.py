class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(None)
        def recr(i, j):
            if i < 0 and j < 0:
                return True
            elif i < 0:
                while j >= 0 and p[j] == '*':
                    j -= 2
                return j < 0
            elif j < 0:
                return False
                
            if p[j] == '*':
                if j == 0:
                    return False
                
                # empty
                if recr(i, j-2):
                    return True
                
                if p[j-1] == '.':
                    for _i in range(i, -1, -1):
                        if recr(_i-1, j-2):
                            return True
                else:
                    for _i in range(i, -1, -1):
                        if s[_i] == p[j-1]:
                            if recr(_i-1, j-2):
                                return True
                        else:
                            break
            elif p[j] == '.' or s[i] == p[j]:
                if recr(i-1, j-1):
                    return True
            else:
                return False
                        
        return recr(len(s)-1, len(p)-1)
                        
                        
                        
                        
                        
                        
                        
