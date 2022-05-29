class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        ans = float('inf')
        n = len(nums)
        
        presum = [0] * (n+1)
        for i, num in enumerate(nums):
            presum[i+1] = presum[i] + num
        
        def dfs(i, cur_max, cur_m):
            nonlocal ans
            if i + cur_m > n:
                return
            
            if cur_m == 1:
                ans = min(ans, max(cur_max, presum[-1] - presum[i]))
                return
            
            for j in range(i, n):
                dfs(j+1, max(cur_max, presum[j+1]-presum[i]), cur_m-1)
        
        dfs(0, 0, m)
        return ans