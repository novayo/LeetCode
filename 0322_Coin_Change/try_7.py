class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def recr(cur_amount):
            if cur_amount < 0:
                return float('inf')
            if cur_amount == 0:
                return 0
            
            ans = float('inf')
            for coin in coins:
                ans = min(ans, recr(cur_amount - coin) + 1)
            return ans
        
        ret = recr(amount)
        return ret if ret < float('inf') else -1
