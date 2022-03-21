class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def isSubsequence(s1, s2):
            i = 0
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    i += 1
                    if i >= len(s1):
                        break
            return i >= len(s1)
        
        def compareString(standard, length, self_index):
            for i in range(length-len(standard)+1):
                target = standard[i:i+length]
                flag = True
                for i, str in enumerate(strs):
                    if i == self_index:
                        continue
                    if len(str) < length:
                        break
                    if isSubsequence(target, str):
                        flag = False
                        break
                
                if flag:
                    return True
            return False
        
        
        strs.sort(key=len, reverse=True)
        length = len(strs[0])
        
        for _length in range(length, 0, -1):
            for i, str in enumerate(strs):
                if len(str) < _length:
                    break
                
                if compareString(strs[i], _length, i):
                    return _length
        return -1
            
        