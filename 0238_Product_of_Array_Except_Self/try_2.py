class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i])
        
        suffix = [nums[-1]]
        for i in range(n-2, -1, -1):
            suffix.append(suffix[-1] * nums[i])
        suffix.reverse()
        
        ans = []
        for i in range(n):
            tmp = 1
            if i > 0:
                tmp *= prefix[i-1]
            if i < n-1:
                tmp *= suffix[i+1]
            ans.append(tmp)
        
        return ans
