class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        hash_table = {}
        used_char = set()
        
        for (s1, s2) in zip(str1, str2):
            in_table = hash_table.get(s1)
            if in_table:
                if hash_table[s1] != s2:
                    return False
            else:
                hash_table[s1] = s2
                used_char.add(s2)
        
        if len(used_char) == 26:
            return False
        return True
