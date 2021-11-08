class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def recr(i, j, memo={}):
            
            if (i, j) in memo:
                return memo[i, j]
            
            if i == -1:
                return j+1
            if j == -1:
                return i + 1
            
            ret = -1
            if word1[i] == word2[j]:
                ret = recr(i-1, j-1)
            else:
                ret = min(
                    recr(i, j-1),
                    recr(i-1, j),
                    recr(i-1, j-1)
                ) + 1
            
            memo[i, j] = ret
            return memo[i, j]
        
        return recr(len(word1)-1, len(word2)-1)
