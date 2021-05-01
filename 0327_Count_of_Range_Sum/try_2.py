class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        找出長度為1~n的sum，把合理的計算近答案即可
        
        1. 先計算長度n，之後往右移動 => TLE
        2. dp把結果存起來，去查詢想要的結果即可
        '''
        ans = 0
        dp = [0] * len(nums)
        
        for cur_length in range(len(nums)):
            for i in range(len(nums) - cur_length):
                dp[i] += nums[i + cur_length]
                if lower <= dp[i] <= upper:
                    ans += 1
        return ans
