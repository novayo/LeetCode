class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        rabbbit
        1111111  t
        1111110  it
        3332100  bit   t[i]
        0000000  bbit
        0000000  abbit
        0000000
        '''
        n = len(s)
        m = len(t)
        dp = [0] * n
        
        # init
        cur = 0
        for j in range(n-1, -1, -1):
            if s[j]==t[-1]:
                cur += 1
            dp[j] = cur
        
        for i in range(1, m):
            tmp = [0] * n
            same = t[m-i-1]
            for j in range(n-i-1, -1, -1):
                if s[j] == same:
                    tmp[j] = tmp[j+1] + dp[j+1]
                else:
                    tmp[j] = tmp[j+1]
            dp = tmp
        return dp[0]