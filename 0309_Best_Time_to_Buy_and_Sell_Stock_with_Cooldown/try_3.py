class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_keep = 0
        keep = cooldown = -float('inf')
        
        for price in prices:
            tmp_not_keep = not_keep
            not_keep = max(tmp_not_keep, cooldown)
            cooldown = keep + price
            keep = max(keep, tmp_not_keep - price)
        
        return max(not_keep, cooldown)