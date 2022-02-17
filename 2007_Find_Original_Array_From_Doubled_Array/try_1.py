class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        '''
        sort + counter
        '''
        
        n = len(changed)
        if n % 2 == 1:
            return []
        
        changed.sort()
        counter = collections.Counter(changed)
        
        ans = []
        for c in changed:
            if c in counter:
                if c*2 not in counter:
                    return []
                
                counter[c] -= 1
                counter[c*2] -= 1
                ans.append(c)
                
                if counter[c] == 0:
                    del counter[c]
                if counter[c*2] == 0:
                    del counter[c*2]
        
        return ans if len(counter) == 0 else []