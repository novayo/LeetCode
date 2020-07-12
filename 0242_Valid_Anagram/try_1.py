class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        直接去看組成是否相同即可
        '''
        return collections.Counter(s) == collections.Counter(t)
