class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Def:
            dp[i][j] = nums1[:i] ~ nums2[:j] 的最長解
        
        Loop:
            dp[i][j] => max(dp[i-1][j], dp[i][j-1])
            if s[i] == t[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        '''
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        
        # loop
        for i in range(1, m+1):
            for j in range(1, n+1):
                n1 = nums1[i-1]
                n2 = nums2[j-1]
                
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if n1 == n2:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                    
        return dp[m][n]
