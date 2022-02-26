class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for length in range(2, n+1):
            res = 0
            for root in range(1, length+1):
                left, right = root-1, length-root
                res += dp[left] * dp[right]
            dp[length] = res
        return dp[n]
