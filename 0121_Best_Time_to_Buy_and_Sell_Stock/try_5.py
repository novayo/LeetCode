class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, cur_min = 0, prices[0]
        for price in prices[1:]:
            cur_min = min(cur_min, price)
            ans = max(ans, price - cur_min)
        return ans

