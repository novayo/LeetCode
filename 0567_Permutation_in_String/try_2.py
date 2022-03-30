class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isMatch(found):
            for key, value in counter.items():
                if key not in found or found[key] != value:
                    return False
            return True
        
        
        if len(s1) > len(s2):
            return False
        
        counter = collections.Counter(s1)
        found = collections.Counter()
        
        # init
        for j in range(len(s1)-1):
            found[s2[j]] += 1
        
        
        # sliding window
        i = 0
        for j in range(len(s1)-1, len(s2)):
            found[s2[j]] += 1
            
            # check if we match s1
            if isMatch(found):
                return True
            
            found[s2[i]] -= 1
            if found[s2[i]] == 0:
                del found[s2[i]]
            i += 1
        
        return False