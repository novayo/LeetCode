class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        no = 0
        have = -float('inf')
        
        for price in prices:
            tmp = no
            no = max(tmp, have+price)
            have = max(have, no-price)
        
        return no
        
