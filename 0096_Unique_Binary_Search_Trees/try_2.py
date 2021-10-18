class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        
        for length in range(2, n+1):
            cur = dp[length-1] * 2
            for pivot in range(2, length):
                left = pivot - 1
                right = length - pivot
                cur += dp[left] * dp[right]
            dp.append(cur)
        
        return dp[-1]