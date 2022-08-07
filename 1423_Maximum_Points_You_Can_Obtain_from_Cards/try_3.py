class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        _sum = sum(cardPoints)
        cur_sum = sum(cardPoints[:n-k])
        ans = _sum - cur_sum
        i = 0
        
        for j in range(n-k, n):
            cur_sum += cardPoints[j] - cardPoints[i]
            ans = max(ans, _sum - cur_sum)
            i += 1
        
        return ans
