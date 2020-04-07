class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i in counter:
            if counter[i] == 1:
                return s.index(i)
        return -1
