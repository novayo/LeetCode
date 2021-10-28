class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i][0] => s[i:] 的最大長度
        # dp[i][1] => 目前總共有幾組
        # i-1 => 找nums[i] < nums[i~n] 的dp[j][0]的最大並統計dp[j][1]
        
        n = len(nums)
        dp = [[0] * 2 for i in range(n)]
        
        # init => 每個人都目前一組
        for i in range(n):
            dp[i][1] = 1
        
        # loop
        for i in range(n-2, -1, -1):
            cur_max = -1
            count = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    if cur_max < dp[j][0]:
                        cur_max = dp[j][0]
                        count = dp[j][1]
                    elif cur_max == dp[j][0]:
                        count += dp[j][1]
                        
            dp[i][0] = cur_max + 1
            dp[i][1] = count
        
        # get ans
        cur_max = -float('inf')
        ans = 0
        for i in range(n):
            if cur_max < dp[i][0]:
                cur_max = dp[i][0]
                ans = dp[i][1]
            elif cur_max == dp[i][0]:
                ans += dp[i][1]
        return ans