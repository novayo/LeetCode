class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        two pointer
        if k < len // 2: find minimum subarray
        else: two pointer
        '''
        
        if k < len(cardPoints) // 2:
            i, j = 0, k-1
            ans = cur_sum = sum(cardPoints[:j+1])
            while i > -k:
                i, j = i-1, j-1
                cur_sum += (cardPoints[i] - cardPoints[j+1])
                ans = max(ans, cur_sum)
        else:
            i, j = 0, len(cardPoints)-k-1
            ans = cur_sum = sum(cardPoints[:j+1])
            while j < len(cardPoints)-1:
                i, j = i+1, j+1
                cur_sum += (cardPoints[j] - cardPoints[i-1])
                ans = min(ans, cur_sum)
            ans = sum(cardPoints) - ans
        return ans
