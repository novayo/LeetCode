class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.defaultdict(int)
        
        for i in range(len(s)):
            counter[s[i]] += 1
        
        if 1 in set(counter.values()):
            for i in range(len(s)):
                if counter[s[i]] == 1:
                    return i
        else:
            return -1
