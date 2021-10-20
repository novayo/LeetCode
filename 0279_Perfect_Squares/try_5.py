class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0 # 平方數
        dp[1] = 1
        
        for cur in range(2, n+1):
            for coin in squares:
                if cur - coin >= 0:
                    dp[cur] = min(dp[cur], dp[cur-coin]+1)
                else:
                    break
        
        return dp[n]