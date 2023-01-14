class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Build presum
        presum = [0] * (n+1)
        for i, num in enumerate(nums):
            presum[i+1] = presum[i] + num
        
        # Get answer
        ans = -float('inf')
        cur_min = presum[0]
        for val in presum[1:]:
            ans = max(ans, val - cur_min)
            cur_min = min(cur_min, val)
            
        return ans

