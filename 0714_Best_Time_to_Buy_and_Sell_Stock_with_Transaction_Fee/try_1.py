class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        idle = 0
        hold = -float('inf')
        
        for price in prices:
            tmp = hold
            hold = max(hold, idle - price)
            idle = max(idle, tmp + price - fee)
        
        return idle