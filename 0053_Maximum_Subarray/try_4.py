class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # presum, 紀錄當前最小, 紀錄最大答案
        presum = 0
        cur_min = float('inf')
        ans = -float('inf')
        
        for num in nums:
            cur_min = min(cur_min, presum)
            presum += num
            ans = max(ans, presum - cur_min)
        return ans
