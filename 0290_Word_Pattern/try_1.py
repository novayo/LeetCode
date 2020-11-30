class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        hash table
        要兩邊都要對應，不然 ab -> aa 會出問題，對右邊來說是相同，但左邊是不同的
        '''
        list_s = s.split(' ')
        
        if len(pattern) != len(list_s):
            return False
        
        pTable = {}
        sTable = {}
        
        for i in range(len(pattern)):
            if pattern[i] in pTable:
                if list_s[i] != pTable[pattern[i]]:
                    return False
            else:
                pTable[pattern[i]] = list_s[i]
            
            if list_s[i] in sTable:
                if pattern[i] != sTable[list_s[i]]:
                    return False
            else:
                sTable[list_s[i]] = pattern[i]
        
        return True
