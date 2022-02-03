class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        
        for i, num in enumerate(nums):
            presum[i+1] = presum[i] + num
        
        l = m = ans = 0
        for i in range(firstLen, n-secondLen+1):
            l = max(l, presum[i]-presum[i-firstLen])
            ans = max(ans, l + presum[i+secondLen] - presum[i])
        
        for i in range(secondLen, n-firstLen+1):
            m = max(m, presum[i]-presum[i-secondLen])
            ans = max(ans, m + presum[i+firstLen]-presum[i])
        
        return ans
