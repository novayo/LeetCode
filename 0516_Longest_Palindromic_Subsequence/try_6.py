class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def recr(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            
            if s[i] == s[j]:
                return recr(i+1, j-1) + 2
            return max(
                recr(i+1, j),
                recr(i, j-1)
            )

        return recr(0, n-1)
