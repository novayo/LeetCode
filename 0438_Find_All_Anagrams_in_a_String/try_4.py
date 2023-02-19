class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        # init - count p
        p_counter = collections.Counter()
        for _c in p:
            p_counter[_c] += 1
        
        # init - count s
        s_counter = collections.Counter()
        for i in range(len(p)):
            s_counter[s[i]] += 1
        
        # find all answer
        ans = []
        i, j = 0, len(p)
        
        if p_counter == s_counter:
            ans.append(0)

        while j < len(s):
            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0:
                del s_counter[s[i]]

            s_counter[s[j]] += 1
            i, j = i+1, j+1
            
            if p_counter == s_counter:
                ans.append(i)
        return ans
            
