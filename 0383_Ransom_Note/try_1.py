class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rcounter = collections.Counter(ransomNote)
        mcounter = collections.Counter(magazine)
        
        for k, v in rcounter.items():
            if k not in mcounter or mcounter[k] < v:
                return False
        return True
