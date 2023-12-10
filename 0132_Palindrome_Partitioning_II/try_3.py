class Solution:
    def minCut(self, s: str) -> int:
        """
        dp[i] => s[0:i]最小切割數
        """
        def isPal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True
        
        
        n = len(s)
        dp = [i for i in range(n)]
        
        if isPal(0, n-1):
            return 0
        
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        
        for i in range(n):
            for j in range(i, n):
                if isPal(i, j):
                    if i == 0:
                        dp[j] = 0
                    else:
                        dp[j] = min(dp[j], dp[i-1]+1)
        
        return dp[n-1]
        
