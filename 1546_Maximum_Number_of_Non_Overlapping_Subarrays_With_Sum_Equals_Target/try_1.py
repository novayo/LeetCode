class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        
        # presum
        for i, num in enumerate(nums):
            presum[i+1] = presum[i] + num
        
        ans = i = 0
        indices = {}
        for j, pre in enumerate(presum):
            t = pre - target
            
            if indices.get(t, -1) >= i:
                ans += 1
                i = j
            
            indices[pre] = j
        return ans