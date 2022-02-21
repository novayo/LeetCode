class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        two pointer with counter
            -> if not in p => delete counter, move i, j to next index
            -> if in p => +1
                -> if exceed, move i
                -> if match, add answer and move i
            
            check counter is match or not in every loop
        '''
        def check_status(counter):
            if len(counter) < len(p):
                return 'normal'
            
            for key, value in counter.items():
                if value > p[key]:
                    return 'exceed'
                elif value < p[key]:
                    return 'normal'
            
            return 'matched'
        
        ans = []
        i = 0
        p = collections.Counter(p)
        counter = collections.Counter()
        
        for j, _s in enumerate(s):
            if _s not in p:
                counter.clear()
                i = j+1
            else:
                counter[_s] += 1
                status = check_status(counter)
                
                while status == 'exceed':
                    counter[s[i]] -= 1
                    i += 1
                    status = check_status(counter)
                
                if status == 'matched':
                    ans.append(i)
                    counter[s[i]] -= 1
                    i += 1
        return ans