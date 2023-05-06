class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def recr(i, j):
            if i >= len(word1) and j >= len(word2):
                memo[i, j] = 0
                return memo[i, j]
            elif i >= len(word1):
                memo[i, j] = len(word2) - j
                return memo[i, j]
            elif j >= len(word2):
                memo[i, j] = len(word1) - i
                return memo[i, j]
            
            if (i, j) in memo:
                return memo[i, j]
            
            if word1[i] == word2[j]:
                memo[i, j] = recr(i+1, j+1)
                return memo[i, j]
            
            memo[i, j] = min(recr(i, j+1), recr(i+1, j), recr(i+1, j+1)) + 1
            return memo[i, j]
        
        return recr(0, 0)
