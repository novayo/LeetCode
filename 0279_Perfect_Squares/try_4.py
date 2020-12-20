class Solution:
    def numSquares(self, n: int) -> int:
        '''
        bottom-up: 從底部往上算，目前的數字最少需要多少的步數，一路算到n，就可以保證n是最少的
        '''
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            tmp = float('inf')
            for j in range(1, int(sqrt(i))+1):
                tmp = min(tmp, dp[i-j*j])
            dp[i] = tmp + 1
        return dp[n]