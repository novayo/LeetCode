class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        a   b   b   c
        dog cat cat dog 
        
        a -> dog
        b -> cat
        
        
        set or hash_table?
        
        set(key)
        hash_table = {key: value}
        ''' 
        # unordered_set<int, int> hash_table1 = new HashMap<int, int>();
        hash_table1 = {} # 被寫好的
        hash_table2 = {}
        
        list_s = s.split(' ')
        
        if len(list_s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            
            if pattern[i] in hash_table1 or list_s[i] in hash_table2:
                expectation1 = hash_table1.get(pattern[i], None)
                expectation2 = hash_table2.get(list_s[i], None)

                if expectation1 != list_s[i] or expectation2 != pattern[i]:
                    return False
        
            hash_table1[pattern[i]] = list_s[i]
            hash_table2[list_s[i]] = pattern[i]
        
        return True
        