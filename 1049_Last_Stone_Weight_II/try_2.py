class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        相撞就是 + or -，不撞就是*0
        所以就是看 任意 + - 0之後，找出>0且最小的結果
        dp[i][j] = 取前i個，看組成j (-sum~sum) 的個數
        
        # 初始條件 
        dp[1][stones[0]] += 1
        dp[1][-stones[0]] += 1
        dp[1][0] += 1
        
        dp[i][j] += dp[i-1][j - stone] # 要+, 所以找上一個+stone = j的
        dp[i][j] += dp[i-1][j + stone] # 要-, 所以找上一個-stone = j的
        dp[i][j] += dp[i-1][j]         # 不動,所以找上一個j的結果
        
        之後再去記得 找出>0且最小的結果
        '''
        n = len(stones)
        s = sum(stones)
        dp = [[0] * (2*s+1) for _ in range(n+1)]
        
        # init
        dp[1][s+stones[0]] += 1
        dp[1][s-stones[0]] += 1
        # dp[1][s+0] += 1
        
        # loop
        for i in range(2, n+1):
            for j in range(-s, s+1):
                stone = stones[i-1]
                
                if j - stone >= -s:
                    dp[i][s+j] += dp[i-1][s+j-stone]
                
                if j + stone <= s:
                    dp[i][s+j] += dp[i-1][s+j+stone]
                
                # dp[i][j] += dp[i-1][s+j] # 不要
                
                if i == n and j >= 0 and dp[i][s+j] > 0:
                    return j
        
        for j in range(0, s+1):
            if dp[n][s+j] > 0:
                return j
