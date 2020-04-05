class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy
        if not prices:
            return 0
        ans = 0
        cur_price = prices[0]
        
        for price in prices[1:]:
            if cur_price > price:
                cur_price = price
            else:
                ans += price - cur_price
                cur_price = price
        return ans
