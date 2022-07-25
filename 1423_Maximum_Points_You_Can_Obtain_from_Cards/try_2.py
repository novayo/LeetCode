class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # O(n) time / O(1) space
        n = len(cardPoints)
        _sum = sum(cardPoints)
        cur_sum = sum(cardPoints[:n-k])
        ans = _sum - cur_sum
        
        for i in range(k):
            cur_sum += cardPoints[n-k+i] - cardPoints[i]
            ans = max(ans, _sum - cur_sum)
        return ans
