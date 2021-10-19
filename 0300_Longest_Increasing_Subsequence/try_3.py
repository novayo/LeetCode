class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for num in nums:
            index = bisect.bisect_left(dp, num)
            
            if index >= len(dp):
                dp.append(num)
            else:
                dp[index] = num
        
        return len(dp)