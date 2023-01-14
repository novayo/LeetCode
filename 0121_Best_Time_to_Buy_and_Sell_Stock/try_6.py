class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] = 0~i的最小值是誰
        n = len(prices)
        
        # Build dp
        dp = [float('inf')] * n
        for i, price in enumerate(prices):
            if i == 0:
                dp[i] = price
            else:
                dp[i] = min(dp[i-1], price)
        
        # Find ans
        ans = 0
        for i in range(n-1, 0, -1):
            ans = max(ans, prices[i] - dp[i-1])
        return ans

