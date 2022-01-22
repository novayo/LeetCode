class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')
        i = 0
        
        while i < len(s1) and i < len(s2):
            if int(s1[i]) < int(s2[i]):
                return -1
            elif int(s1[i]) > int(s2[i]):
                return 1
            i += 1
        
        while i < len(s1):
            if int(s1[i]) > 0:
                return 1
            i += 1
        
        while i < len(s2):
            if int(s2[i]) > 0:
                return -1
            i += 1
            
        return 0
