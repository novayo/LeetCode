class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getHash(string):
            ret = 1
            for s in string:
                tmp = 2**ord(s)
                if ret & tmp:
                    ret += 31415926//ord(s)
                ret |= tmp
            return ret
        
        table = collections.defaultdict(list)
        for s in strs:
            table[getHash(s)].append(s)
        
        return list(table.values())
