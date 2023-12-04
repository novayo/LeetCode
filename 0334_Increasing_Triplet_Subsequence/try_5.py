class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            
            if idx >= len(dp):
                dp.append(num)
            else:
                dp[idx] = num
            
            if len(dp) >= 3:
                return True
        return False
        
