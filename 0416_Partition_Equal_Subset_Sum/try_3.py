class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        看看能不能拿一半，背包問題
        dp[i][j] = 在第i位置之前，背包容量為j => 能裝滿嗎?
        最後要找 dp[len(nums)-1][sum(nums)//2]
        
        dp[0][j] = False
        dp[i][0] = True
        
        nums[i]時 => 不拿 => dp[i][j] = dp[i-1][j]
                     拿   => dp[i][j] = dp[i][j-nums[i]]
        
        '''
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        s = s // 2
        
        n = len(nums)
        dp = [False] * (s+1)
        
        # init
        dp[0] = True
        
        # loop
        for i in range(n):
            for j in range(s, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
        
        return dp[s]
                    