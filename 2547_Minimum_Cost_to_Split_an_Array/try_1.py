class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        L = len(nums)
        trimmed_dict = {}
        for i in range(L):
            current, counter = 0, {}
            for j in range(i+1, L+1):
                num = nums[j-1]
                if num not in counter:
                    counter[num] = 1
                else:
                    if counter[num] == 1:
                        current += 1
                    counter[num] += 1
                    current += 1
                trimmed_dict[i, j] = current
        
        
        dp = [float('inf')] * (L+1)
        dp[L] = 0
        for i in range(L-1, -1, -1):
            ans = float('inf')
            for j in range(i+1, L+1):
                ans = min(ans, k + trimmed_dict[i, j] + dp[j])
            dp[i] = ans
        return dp[0]

