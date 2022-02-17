class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        '''
        sort + counter
        '''
        
        n = len(changed)
        if n % 2 == 1:
            return []
        
        counter = collections.Counter(changed)
        
        ans = []
        for c in sorted(counter.keys()):
            if c not in counter:
                continue
            
            if counter[c] > counter[c*2]:
                return []
            
            if c == 0:
                ans += [0] * (counter[c] // 2)
            else:
                counter[c*2] -= counter[c]
                ans += [c] * counter[c]
                
            del counter[c]
            if counter[c*2] == 0:
                del counter[c*2]
        
        return ans if len(counter) == 0 else []