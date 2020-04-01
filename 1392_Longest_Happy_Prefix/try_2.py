class Solution:
    def longestPrefix(self, s: str) -> str:
        # KMP createPrefixTable
        def createPrefixTable(string):
            ret = [0] * len(string)
            _len = 0
            i = 1
            
            while i < len(string):
                if string[i] == string[_len]:
                    _len += 1
                    ret[i] = _len
                    i += 1
                else:
                    if _len != 0:
                        _len = ret[_len-1]
                    else:
                        i += 1
            return ret
        
        
        prefixTable = createPrefixTable(s)
        return s[:prefixTable[-1]]
