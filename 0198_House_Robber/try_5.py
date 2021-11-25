class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        搶 不搶
        dp[i][0] => 搶
        dp[i][1] => 不搶
        
        dp[i][0] = dp[i-1][1] + num
        dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        '''
        n = len(nums)
        dp = [[0] * 2 for _ in range(n+1)]
        
        dp[0][0] = -float('inf')
        
        for i in range(1, n+1):
            num = nums[i-1]
            
            dp[i][0] = dp[i-1][1] + num
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        
        return max(dp[n])
        
