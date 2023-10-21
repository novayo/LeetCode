class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for side_length in range(int(sqrt(n+1))+1):
            square = side_length ** 2
            for val in range(n+1):
                if square > val:
                    continue
                dp[val] = min(dp[val], dp[val - square] + 1)
        
        return dp[n]
        
