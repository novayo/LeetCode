class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def recr(i, cur_amount):
            if cur_amount == 0:
                return 1
            if cur_amount < 0 or i >= len(coins):
                return 0
            
            if cur_amount < coins[i]:
                return recr(i + 1, cur_amount)
            else:
                return recr(i + 1, cur_amount) + recr(i, cur_amount - coins[i])
        
        return recr(0, amount)
