class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        
        # get min(prices[:i-1])
        cur_min = float('inf')
        for i in range(n):
            dp[i] = cur_min
            cur_min = min(cur_min, prices[i])
        
        # get answer
        ans = 0
        for i in range(n):
            ans = max(ans, prices[i] - dp[i])
        return ans
