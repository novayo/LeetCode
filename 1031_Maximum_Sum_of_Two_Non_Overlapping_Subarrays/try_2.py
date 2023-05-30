class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        ans = left_max = -float('inf')
        for i in range(firstLen, len(presum) - secondLen):
            left_max = max(left_max, presum[i] - presum[i-firstLen])
            right = presum[i+secondLen] - presum[i]
            ans = max(ans, left_max + right)
        
        left_max = -float('inf')
        for i in range(secondLen, len(presum) - firstLen):
            left_max = max(left_max, presum[i] - presum[i-secondLen])
            right = presum[i+firstLen] - presum[i]
            ans = max(ans, left_max + right)

        return ans
            
