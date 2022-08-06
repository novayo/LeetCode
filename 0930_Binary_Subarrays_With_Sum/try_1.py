class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        
        
        ans = 0
        counter = collections.Counter()
        for num in presum:
            ans += counter[num - goal]
            counter[num] += 1
        return ans
