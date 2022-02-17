class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        LIS: 往前找第一個能整除的+1即可
        '''
        nums.sort()
        n = len(nums)
        dp = [[] for _ in range(n)]
        
        for i, num in enumerate(nums):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    if len(dp[j]) > len(dp[i]):
                        dp[i] = dp[j].copy()
            dp[i].append(num)
        
        ans = []
        for v in dp:
            if len(ans) < len(v):
                ans = v
        return ans