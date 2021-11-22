class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        dp[i][j] = 前i個能否組成j = True
        '''
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        s //= 2
        dp = [[False] * (s+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, s+1):
                if j >= nums[i-1]:
                    '''
                    為什麼這裡要dp[i-1][j-nums[i-1]]
                    '''
                    dp[i][j] = dp[i][j] or dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[n][s]
