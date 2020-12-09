class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        
        for string in strings:
            base = ord(string[0])
            
            tmpList = []
            for s in string:
                tmp = ord(s) - base
                if tmp < 0:
                    tmp += 26
                tmpList.append(tmp)
            
            table[tuple(tmpList)].append(string)
        
        return table.values()