class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idle = 0
        cooldown = hold = -float('inf')
        
        for price in prices:
            tmp  = hold
            hold = max(hold, idle - price)
            idle = max(idle, cooldown)
            cooldown = tmp + price
        
        return max(cooldown, idle)