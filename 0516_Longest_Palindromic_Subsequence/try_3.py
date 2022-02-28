class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        (x)bottom-up回來之後，去添加所有可能，並計算答案
        如果i-1==j+1 => i~j看是不是回文，如果是，則i-1~j+1也是
        '''
        n = len(s)
        ans = 0
        
        memo = {}
        def recr(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            
            if (i, j) in memo:
                return memo[i, j]
            
            if s[i] == s[j]:
                memo[i, j] = recr(i+1, j-1) + 2
            else:
                memo[i, j] = max(recr(i+1, j), recr(i, j-1))
            return memo[i, j]
        
        return recr(0, n-1)

