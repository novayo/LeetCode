class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)

        if sum([val % 2 == 1 for val in counter.values()]) >= 2:
            return []
        
        # 找出奇數的值, 放中間
        odd = ""
        for key in counter:
            if counter[key] % 2 == 1:
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
                odd = key
                break

        def recr(counter):
            if not counter:
                return [odd]
            
            ans = []
            keys = list(counter.keys())
            for key in keys:
                counter[key] -= 2
                if counter[key] == 0:
                    del counter[key]
                
                for val in recr(counter):
                    ans.append(key + val + key)
                
                counter[key] += 2
            return ans
        
        return recr(counter)
