class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        '''
        shift 到a開頭
        '''
        # O(len(string))
        def shift_string_to_a_prefix(string):
            shift = (26-(ord(string[0])-ord('a'))) % 26
            
            ret = ''
            for s in string:
                ret += chr((ord(s)-ord('a') + shift)%26 + ord('a'))
            return ret
        
        tables = collections.defaultdict(list)
        for string in strings:
            s = shift_string_to_a_prefix(string)
            tables[s].append(string)

        return list(tables.values())
        
