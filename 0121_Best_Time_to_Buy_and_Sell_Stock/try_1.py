class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(index):
            start, pre = index, prices[index]
            for j in range(index, len(prices)):
                if pre >= prices[j]:
                    pre = prices[j]
                    start = j
                    continue
                else:
                    return start
            return -1
        
        ans, i = 0, 0
        while i < len(prices):
            i = helper(i)
            if i == -1: break
            else: i += 1
            ans = max(ans, max(prices[i:]) - prices[i-1])
        return ans
