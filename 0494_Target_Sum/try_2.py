class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        dp[i][j] = 使用前i個，能組成j的 = 有n種
        
        dp[i][j] += dp[i-1][j-nums[i]]
        dp[i][j] += dp[i-1][j+nums[i]]
        '''
        n = len(nums)
        _sum = sum(nums)
        dp = {}
        
        dp[0] = collections.defaultdict(int)
        dp[0][-nums[0]] += 1
        dp[0][nums[0]] += 1
        
        for i in range(1, n):
            if i not in dp:
                dp[i] = collections.defaultdict(int)
            
            # loop 
            for j in range(-_sum, _sum+1):
                dp[i][j] += dp[i-1][j+nums[i]]
                dp[i][j] += dp[i-1][j-nums[i]]
        
        return dp[n-1][target]
