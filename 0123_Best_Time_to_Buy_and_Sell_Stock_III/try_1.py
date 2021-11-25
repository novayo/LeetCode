class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][0] = 持有第一張 (維持 原本無持有然後買)
        dp[i][1] = 沒有第一張 (維持 賣掉第一張) 
        dp[i][2] = 持有第二張 (維持 第一張賣掉然後買) 
        dp[i][3] = 沒有第二張 (維持 賣掉第二張) 
        
        dp[i][0] = max(dp[i-1][0], 0-price)
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+price)
        dp[i][2] = max(dp[i-1][2], dp[i-1][1]-price)
        dp[i][3] = max(dp[i-1][3], dp[i-1][2]+price)
        '''
        n = len(prices)
        dp = [[0] * 4 for _ in range(n+1)]
        
        dp[0][0] = -float('inf')
        dp[0][2] = -float('inf')
        
        for i in range(1, n+1):
            price = prices[i-1]
            
            dp[i][0] = max(dp[i-1][0], 0 - price)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+price) # 第一次不能獲利 => dp[0][0] = -float('inf')
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]-price)
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]+price) # 第一次不能獲利 => dp[0][2] = -float('inf')
            
        return max(dp[n])
