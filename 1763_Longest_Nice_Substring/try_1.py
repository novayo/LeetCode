class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def recr(string):
            if len(string) < 2:
                return ""
            cache = set(string)
            for i, c in enumerate(string):
                if c.upper() in cache and c.lower() in cache:
                    continue
                
                left = recr(string[:i])
                right = recr(string[i+1:])
                return left if len(left) >= len(right) else right
            return string
        
        return recr(s)