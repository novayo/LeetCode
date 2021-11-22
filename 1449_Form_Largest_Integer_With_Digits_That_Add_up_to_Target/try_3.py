class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        '''
        dp[i][j] = 前i個，組成j的字串是什麼(留最大)
        
        # 初始條件 => 應該沒有
        
        dp[i][j] = max(
            dp[i-1][j], # 不選
            dp[i][j-cost] + str(cost)
        )
        '''
        
        def compare(s1, s2):
            if s1 == '':
                return s2
            if s2 == '':
                return s1
            
            # s2 = ''.join(sorted(s2, reverse=True))
            if int(s1) >= int(s2):
                return s1
            else:
                return s2
        
        n = len(cost)
        dp = [[''] * (target+1) for _ in range(n+1)]
        
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                c = cost[i-1]
                
                if j == c:
                    dp[i][j] = compare(dp[i-1][j], str(i))
                elif j > c and dp[i][j-c] != '':
                    dp[i][j] = compare(dp[i-1][j], str(i) + dp[i][j-c])
                else:
                    dp[i][j] = dp[i-1][j]
                dp[i][j] = ''.join(sorted(dp[i][j], reverse=True))
        
        return dp[n][target] if dp[n][target] != '' else '0'
