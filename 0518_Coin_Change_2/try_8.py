class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for val in range(amount+1):
                if coin > val:
                    continue
                dp[val] += dp[val - coin]
        return dp[amount]
        
