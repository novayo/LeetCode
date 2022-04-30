class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        conversion = {}
        for s1, s2 in zip(str1, str2):
            if s1 in conversion and conversion[s1] != s2:
                return False
            conversion[s1] = s2
        
        return len(set(str2)) < 26
