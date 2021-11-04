class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        
        # presum
        for i in range(1, n+1):
            dp[i] = nums[i-1] + dp[i-1]
        
        # 往前查找需要的值的個數
        ans = 0
        d = collections.defaultdict(int)
        for i in range(n+1):
            ans += d.get(dp[i] - k, 0)
            d[dp[i]] += 1
        
        return ans
