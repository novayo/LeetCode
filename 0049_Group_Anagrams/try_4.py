class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = collections.defaultdict(list)
        for s in strs:
            cnt = collections.Counter(s)
            key_s = ""
            for a in range(97, 97+26):
                a = chr(a)
                if a in cnt:
                    key_s += f"{a}{cnt[a]}"
            
            collection[key_s].append(s)
        
        return list(collection.values())    

