class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        pcounter = collections.Counter(s1)
        ans = []
        while j <= len(s2):
            if pcounter == collections.Counter(s2[i:j]):
                return True
            i += 1
            j += 1
        return False
