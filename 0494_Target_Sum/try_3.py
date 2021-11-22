class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        要 + or - => 求個數
        
        dp[i][j] = 前i個，組成j的 = n 種
        
        # 初始條件
        dp[1][nums[0]] += 1
        dp[1][-nums[0]] += 1
        
        dp[i][j] += dp[i-1][j-nums[0]]
        dp[i][j] += dp[i-1][j+nums[0]]
        '''
        n = len(nums)
        s = sum(nums)
        
        if target > s:
            return 0
        
        dp = [[0] * (2*s+1) for _ in range(n+1)]
        
        dp[1][s+nums[0]] += 1
        dp[1][s+-nums[0]] += 1
        
        for i in range(1, n+1):
            for j in range(-s, s+1):
                if j - nums[i-1] >= -s:
                    dp[i][s+j] += dp[i-1][s+j-nums[i-1]]
                if j + nums[i-1] <= s:
                    dp[i][s+j] += dp[i-1][s+j+nums[i-1]]
        
        return dp[n][s+target]
