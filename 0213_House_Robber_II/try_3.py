class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        0~n-1   搶一次
        1~n     搶一次
        求這之中最大
        
        dp[i][0] => 搶
        dp[i][1] => 不搶
        
        
        dp[i][0] = dp[i-1][1] + num
        dp[i][1] = max(dp[i-1][1], dp[i-1][0])
        '''
        
        def helper(offset):
            n = len(nums) - 1
            dp = [[0] * 2 for _ in range(n+1)]
            dp[0][0] = -float('inf')
            
            for i in range(1, n+1):
                num = nums[i-1+offset]
                
                dp[i][0] = dp[i-1][1] + num
                dp[i][1] = max(dp[i-1][1], dp[i-1][0])
            
            return max(dp[n])
        
        # 若只有一個沒有前後之分
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(0), helper(1))
        
