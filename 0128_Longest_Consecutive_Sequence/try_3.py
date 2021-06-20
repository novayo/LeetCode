class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = {}
        nums_set = set(nums)
        
        ans = 0
        for num in nums:
            tmp_num = num
            
            count = 0
            while tmp_num in nums_set:
                if tmp_num in dp:
                    count += dp[tmp_num]
                    break
                count += 1
                tmp_num += 1
            dp[num] = count
            ans = max(ans, dp[num])
        
        return ans