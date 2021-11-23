class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        '''
        sum / n = sumA / k = sumB / (n-k)
        sum / n * k = sumA
        
        dp[i][k][n] = 前i個，取k個，能否組成n = False => 這個代表sumA
        
        dp[i][0][0] = True
        
        if n >= nums[i]:
            dp[i][k][n] |= dp[i-1][k][n] | dp[i-1][k-1][n-nums[i]]
        else:
            dp[i][k][n] |= dp[i-1][k][n]
        
        for k in range(1, n):
            for sumA in range(1, sum):
                if dp[i][k][sumA] == True and sum * k / n == sumA:
                    return True
        return False
        '''
        sum_num = sum(nums)
        n = len(nums)
        
        dp = [[[False] * (sum_num+1) for _ in range(n//2+1)] for __ in range(n+1)]
        
        # init
        for i in range(n+1):
            dp[i][0][0] = True
        
        # loop
        for i in range(1, n+1):
            for k in range(1, n//2+1):
                for sumA in range(1, sum_num+1):
                    if sumA >= nums[i-1]:
                        dp[i][k][sumA] = dp[i][k][sumA] or dp[i-1][k][sumA] or dp[i-1][k-1][sumA - nums[i-1]]
                    else:
                        dp[i][k][sumA] = dp[i][k][sumA] or dp[i-1][k][sumA]
        
        # check ans
        for k in range(1, n//2+1):
            for sumA in range(1, sum_num):
                if sum_num * k / n == sumA and dp[n][k][sumA] == True:
                    return True
        return False
        
