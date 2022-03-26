class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # LIS
        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index >= len(dp):
                dp.append(num)
            else:
                dp[index] = num
            
            if len(dp) >= 3:
                return True
        return False
