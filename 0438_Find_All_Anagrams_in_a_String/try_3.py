class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def counter_plus_1(table, value):
            if value not in table:
                table[value] = 0
            table[value] += 1
        
        def counter_minus_1(table, value):
            table[value] -= 1
            if table[value] == 0:
                del table[value]
        
        
        if len(s) < len(p):
            return []
        
        # init - count p
        p_counter = {}
        for _c in p:
            counter_plus_1(p_counter, _c)
        
        # init - count s
        s_counter = {}
        for i in range(len(p)):
            counter_plus_1(s_counter, s[i])
        
        # find all answer
        ans = []
        i, j = 0, len(p)
        
        if p_counter == s_counter:
            ans.append(0)

        while j < len(s):
            counter_minus_1(s_counter, s[i])
            counter_plus_1(s_counter, s[j])
            i, j = i+1, j+1
            
            if p_counter == s_counter:
                ans.append(i)
        return ans
            
