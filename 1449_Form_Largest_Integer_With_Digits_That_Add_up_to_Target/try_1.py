class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def compare(a, b):
            if a == '':
                return b
            else:
                a = ''.join(sorted(a, reverse=True))
                _a = int(a)
            
            if b == '':
                return a
            else:
                b = ''.join(sorted(b, reverse=True))
                _b = int(b)
            
            if _a >= _b:
                return a
            else:
                return b
        
        m = len(cost)
        dp = [['' for _m in range(target+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, target+1):
                c = cost[i-1]

                dp[i][j] = dp[i-1][j]
                if j == c:
                    dp[i][j] = compare(dp[i][j], str(i))
                elif j > c and dp[i][j-c] != '':
                    dp[i][j] = compare(dp[i][j], dp[i][j-c] + str(i))
        
        dp[m][target] = ''.join(sorted(dp[m][target], reverse=True))
        return dp[m][target] if dp[m][target] != '' else '0'
