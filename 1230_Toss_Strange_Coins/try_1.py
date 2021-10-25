class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # [i][j] => 投了i次，有j個向上的機率
        dp = [[0] * (target+1) for i in range(len(prob)+1)]
        
        # init => 全空
        dp[0][0] = 1
        for i in range(1, len(prob)+1):
            dp[i][0] = dp[i-1][0] * (1-prob[i-1])
        
        
        for i in range(1, len(prob)+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j] * (1-prob[i-1]) + dp[i-1][j-1] * prob[i-1]
        
        return dp[-1][-1]