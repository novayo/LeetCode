class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one pass
        ans, _min = 0, float('inf')
        for i in prices:
            if _min > i:
                _min = i
            elif i - _min > ans:
                ans = i - _min
        return ans
