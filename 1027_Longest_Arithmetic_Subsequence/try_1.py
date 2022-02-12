class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        dp[index][diff] = count
        '''
        ans = 0
        dp = {}
        for i, num in enumerate(nums):
            dp[i] = collections.defaultdict(lambda: 1)
            
            for j, pre in enumerate(nums[:i]):
                diff = num-pre
                
                dp[i][diff] = dp[j][diff] + 1
                ans = max(ans, dp[i][diff])
        
        return ans
