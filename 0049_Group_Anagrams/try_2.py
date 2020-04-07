class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-97] += 1
            table[tuple(key)].append(s)
        return table.values()
