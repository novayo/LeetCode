class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for cur in range(1, amount+1):
            for coin in coins:
                if cur - coin >= 0:
                    dp[cur] += dp[cur-coin]
        
        return dp[amount]