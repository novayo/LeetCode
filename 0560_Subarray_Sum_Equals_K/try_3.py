class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # presum
        dp = [0] *  (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]+nums[i-1]
        
        # find k => two sum
        ans = 0
        table = collections.defaultdict(int)
        table[0] = 1
        for value in dp[1:]:
            target = value-k
            ans += table[target]
            table[value] += 1
        
        return ans
