class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming
        dp = collections.defaultdict(int)
        dp[0] = 1
        dp[1] = 1
        
        # depart
        def recur(steps):
            exist = dp.get(steps)
            if exist: return exist
            dp[steps] = recur(steps-1) + recur(steps-2)
            return dp[steps]
            
        return recur(n)
