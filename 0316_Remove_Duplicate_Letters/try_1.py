class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        index = {}
        for i in range(n-1, -1, -1):
            if s[i] in index:
                continue
            index[s[i]] = i
        
        
        ans = ''
        start = 0
        while len(index) > 0:
            end = min(index.values())
            
            char = 'z'
            for i in range(start, end+1):
                _s = s[i]
                if _s in index and _s < char:
                    char = _s
                    start = i+1
            
            ans += char
            del index[char]
        
        return ans    
