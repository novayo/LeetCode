class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def recr(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            return max(
                recr(i+1, j+1) + int(text1[i] == text2[j]),
                recr(i, j+1),
                recr(i+1, j)
            )
        
        return recr(0, 0)
        
