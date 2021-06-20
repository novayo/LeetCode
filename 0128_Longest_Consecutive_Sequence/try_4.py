class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = {}
        nums_set = set(nums)
        
        ans = 0
        while nums_set:
            num = nums_set.pop() # remove num
            tmp_num = num + 1    # look at num + 1
            
            count = 1 # num is counted
            while tmp_num in nums_set:
                nums_set.remove(tmp_num)
                if tmp_num in dp:
                    count += dp[tmp_num]
                    break
                count += 1
                tmp_num += 1
            
            dp[num] = count + dp.get(tmp_num, 0) # num ~ bigger than num
            ans = max(ans, dp[num])
        
        return ans