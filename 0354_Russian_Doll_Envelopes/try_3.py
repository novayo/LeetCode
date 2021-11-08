class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        dp = []
        for w, h in envelopes:
            index = bisect.bisect_left(dp, h)
            if index >= len(dp):
                dp.append(h)
            else:
                dp[index] = h
        return len(dp)

