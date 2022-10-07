class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        
        @functools.lru_cache(None)
        def recr(i):
            if i == n:
                return 0
            
            length = n-i+1
            ans = 0
            for k in range(1, length//2+1):
                if n-(i+k)+1 <= ans:
                    break
                if s[i:i+k] == s[i+k:i+k+k]:
                    ans = max(ans, recr(i+k))
                    
            return ans + 1
        
        return recr(0)