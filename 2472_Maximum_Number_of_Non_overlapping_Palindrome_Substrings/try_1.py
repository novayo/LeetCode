class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def pal(i, j):
            if j >= len(s):
                return False
            return s[i:j+1] == s[i:j+1][::-1]
        
        @functools.lru_cache
        def recr(i):
            if i + k > len(s):
                return 0
            
            ans = recr(i+1)
            if pal(i, i+k-1):
                ans = max(ans, 1+recr(i+k))
            if pal(i, i+k):
                ans = max(ans, 1+recr(i+k+1))
            
            return ans
        return recr(0)