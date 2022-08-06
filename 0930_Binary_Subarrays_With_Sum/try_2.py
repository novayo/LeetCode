class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # O(n) time / O(n) space
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        ans = 0
        counter = collections.Counter()
        for val in presum:
            ans += counter[val - goal]
            counter[val] += 1
        
        return ans