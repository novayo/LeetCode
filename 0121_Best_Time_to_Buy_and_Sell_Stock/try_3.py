class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [float('inf')] * len(prices)
        
        ans = 0
        for i in range(len(prices)):
            dp[i] = min(dp[i-1], prices[i])
            ans = max(ans, prices[i] - dp[i])
        
        return ans