class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        '''
        dp1 = values[i] + i
        dp2 = values[j] - j
        dp3 = min(dp2[i+1:])
        '''
        n = len(values)
        
        # build dp
        dp1 = [0] * n
        dp2 = [0] * n
        dp3 = [0] * n
        
        for i, v in enumerate(values):
            dp1[i] = v+i
        
        for i, v in enumerate(values):
            dp2[i] = v-i
        
        cur_max = -float('inf')
        for i in range(n-1, -1, -1):
            dp3[i] = cur_max
            cur_max = max(cur_max, dp2[i])
        
        # get answer
        ans = 0
        for a, b in zip(dp1, dp3):
            ans = max(ans, a + b)
        
        return ans
