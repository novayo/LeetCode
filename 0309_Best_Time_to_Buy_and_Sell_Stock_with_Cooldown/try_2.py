class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        第i天
        dp[i][0] => 剛賣
        dp[i][1] => 賣一天以上
        dp[i][2] => 剛買（擁有）
        
        dp[i][0] = dp[i-1][2] + prices[i]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
        '''
        n = len(prices)
        dp = [[0] * 3 for _ in range(n+1)]
        
        dp[0][2] = -float('inf')
        
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][2] + prices[i-1]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i-1])
        
        return max(dp[n])
        
