class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for val in range(amount+1):
                if coin > val:
                    continue
                dp[val] = min(dp[val], dp[val - coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1
