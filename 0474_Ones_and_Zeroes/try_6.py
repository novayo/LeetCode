class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for s in strs:
            counter = collections.Counter(s)
            
            for i in range(m-counter["0"]+1):
                for j in range(n-counter["1"]+1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i+counter["0"]][j+counter["1"]])
        
        return dp[0][0]
        
