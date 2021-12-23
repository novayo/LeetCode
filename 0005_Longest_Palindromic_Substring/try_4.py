class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        dp[i:j] = string[i:j] 是否為回文
        
        => dp[i-1:j+1] = string[i-1] == string[j+1] and string[i:j] == True
        => len(string[i:j]) <= 2 and string[i] == string[j] => True
        '''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        max_length = [0, 0]
        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                if i == j:
                    dp[i][j] = True
                else:
                    if s[i] == s[j] and (j-i+1 == 2 or dp[i+1][j-1]):
                        dp[i][j] = True
                
                if dp[i][j] == True and j-i > max_length[1]-max_length[0]:
                    max_length[0], max_length[1] = i, j
        
        return s[max_length[0]:max_length[1]+1]
                