class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        
        presum = [0] * (n+1)
        for i, num in enumerate(nums):
            presum[i+1] = presum[i] + num
        
        memo = {}
        def dfs(i, cur_m):
            if i + cur_m > n:
                return float('inf')
            
            if cur_m == 1:
                return presum[-1] - presum[i]
            
            if (i, cur_m) not in memo:
                ret = float('inf')
                for j in range(i, n):
                    m = presum[j+1]-presum[i]
                    ret = min(ret, max(m, dfs(j+1, cur_m-1)))
                memo[i, cur_m] = ret
            return memo[i, cur_m]
            
        return dfs(0, m)