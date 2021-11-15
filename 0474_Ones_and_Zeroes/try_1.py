class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        可以先整理成 0, 1個有幾個
        之後就變成背包問題
        
        dp[i][j][k] = 前i個, 當最大為j個1, k個0時 = 最多有幾種
        
        dp[0][0][k] = 0
        dp[0][j][0] = 0
        dp[i][0][0] = 0
        
        for i in range(len(strs)):
            for j in range(m+1):
                for k in range(n+1):
                    target_0 = strs[0].get0()
                    target_1 = strs[0].get1()
                    
                    # 這個題目是 要馬都加上去，要馬就不加
                    if j - zeros >= 0 and k - ones >= 0:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        
        return dp[len(strs)][m][n]
        '''
        mapping = []
        for s in strs:
            counter = Counter(s)
            mapping.append((counter['0'], counter['1']))
        
        length = len(strs)
        dp = [[[0] * (n+1) for i in range(m+1)] for j in range(length+1)]
        
        # loop
        for i in range(1, length+1):
            for j in range(m+1):
                for k in range(n+1):
                    zeros = mapping[i-1][0]
                    ones  = mapping[i-1][1]
                    
                    if j - zeros >= 0 and k - ones >= 0:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        
        return dp[length][m][n]
