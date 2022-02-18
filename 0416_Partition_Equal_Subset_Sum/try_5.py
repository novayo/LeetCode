class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        get sum first
        and find if exsists half of sum
        
        backpack => 使用前i個看是否能組成j
        '''
        n = len(nums)
        s = sum(nums)
        
        if s % 2 == 1:
            return False
        
        s = s // 2
        dp = [[False] * (s+1) for _ in range(n+1)]
        
        # init
        for i in range(n+1):
            dp[i][0] = True
        
        # loop
        for i in range(1, n+1):
            for j in range(1, s+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[-1][-1]
        