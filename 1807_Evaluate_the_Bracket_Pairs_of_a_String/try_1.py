class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # O(len(s) + len(knowledge)) time / O(len(knowledge)) space
        cache = {}
        ptr = i = 0
        ans = ''
        
        while i < len(s):
            if s[i] != '(':
                ans += s[i]
            else:
                i += 1
                key = ''
                while s[i] != ')':
                    key += s[i]
                    i += 1
                
                while ptr < len(knowledge) and key not in cache:
                    cache[knowledge[ptr][0]] = knowledge[ptr][1]
                    ptr += 1
                
                if key in cache:
                    ans += cache[key]
                else:
                    ans += '?'
            i += 1
        return ans