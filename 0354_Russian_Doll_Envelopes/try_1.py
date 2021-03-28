class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # dp
        envelopes.sort()
        
        ans = 0
        dp = [0] * len(envelopes)
        for i in range(len(envelopes)-1, -1, -1):
            val = 0
            for j in range(i+1, len(envelopes)):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    val = max(val, dp[j])
            dp[i] = val + 1
            ans = max(ans, dp[i])
        
        return ans