class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        '''
        O(n) time / O(n) space
        - n is the length of the input array
        '''
        n = len(values)
        dp = [-1] * n
        
        # init dp[i]: max(i~end) for (values[j] - j)
        cur_max = -float('inf')
        for i in range(n-1, -1, -1):
            cur_max = max(cur_max, values[i] - i)
            dp[i] = cur_max
        
        # get answer
        ans = -float('inf')
        for i in range(n-1):
            ans = max(ans, values[i] + i + dp[i+1])
        return ans
