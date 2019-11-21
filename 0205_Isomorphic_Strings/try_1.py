class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = collections.defaultdict(list)
        t_dict = collections.defaultdict(list)
        
        for i in range(len(s)):
            s_dict[s[i]].append(i)
            t_dict[t[i]].append(i)
        return list(s_dict.values()) == list(t_dict.values())
