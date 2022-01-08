class Solution:
    def numSquares(self, n: int) -> int:
        '''
        先找出所有可行的square
        
        => 用最少coin組成n => coin change
        
        dp[i][j] = 用前i個，組成j的最少個數
        '''        
        
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        
        for i in range(2, n+1):
            tmp = float('inf')
            for j in range(1, int(math.sqrt(i)) + 1):
                tmp = min(tmp, dp[i-j*j])
            dp[i] = tmp + 1
        
        return dp[n]

