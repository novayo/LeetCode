class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def recr(mid):
            nonlocal ans
            
            if len(mid) == n:
                ans.append(mid)
                return
        
            for key, value in counter.items():
                if value >= 2:
                    counter[key] -= 2
                    recr(key + mid + key)
                    counter[key] += 2
            
            
        
        n = len(s)
        
        counter = collections.Counter(s)
        odd = []
        for key, value in counter.items():
            if value % 2 == 1:
                odd.append(key)
        
        ans = []
        if len(odd) > 1:
            return []
        elif len(odd) == 1:
            recr(odd[0])
        else:
            recr('')
        return ans
        
