class Solution:
    def tribonacci(self, n: int) -> int:
        def _tribonacci(num):
            nonlocal dp
            if num in dp: 
                return dp[num]
            dp[num] = _tribonacci(num-1) + _tribonacci(num-2) + _tribonacci(num-3)
            return dp[num]
        
        dp = {0:0, 1:1, 2:1}
        _tribonacci(n)
        return dp[n]
