class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        
        cur = 0
        for i in range(n):
            prefix[i] = cur
            if nums[i] == 1:
                cur += 1
            else:
                cur = 0
        
        cur = 0
        for i in range(n-1, -1, -1):
            suffix[i] = cur
            if nums[i] == 1:
                cur += 1
            else:
                cur = 0
        
        ans = 0
        for i in range(n):
            ans = max(ans, 1 + prefix[i] + suffix[i]) # 0當作1，1也當作1
        
        return ans