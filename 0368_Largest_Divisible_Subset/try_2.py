class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        dp[i] = 第i個元素之前（包含），最多有幾個可以整除
        '''
        nums.sort() # 防止重複找尋 & 用大的當分子求是否可以整除
        n = len(nums)
        dp = []
        
        # init
        for num in nums:
            dp.append([num])
        
        # loop
        ans = []
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    # 若之前的選擇加上自己 比 現在的大，則留最大
                    if len(dp[i]) <= len(dp[j]) + 1:
                        dp[i] = dp[j]+[nums[i]]
            
            # 紀錄過程中最佳解
            if len(ans) < len(dp[i]):
                ans = dp[i]
        return ans
