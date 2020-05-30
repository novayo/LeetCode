class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j = len(p)
        pcounter = collections.Counter(p)
        ans = []
        while j <= len(s):
            if pcounter == collections.Counter(s[i:j]):
                ans.append(i)
            i += 1
            j += 1
        return ans
