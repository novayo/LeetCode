class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_left_dp(row):
            dp = [0] * n
            dp[0] = row[0]
            for j in range(1, n):
                dp[j] = max(dp[j-1]-1, row[j])
            return dp
        
        def get_right_dp(row):
            dp = [0] * n
            dp[-1] = row[-1]
            for j in range(n-2, -1, -1):
                dp[j] = max(dp[j+1]-1, row[j])
            return dp
        
        m = len(points)
        n = len(points[0])
        
        for i in range(1, m):
            left_dp = get_left_dp(points[i-1])
            right_dp = get_right_dp(points[i-1])
            for j in range(n):
                points[i][j] += max(left_dp[j], right_dp[j])
        
        return max(points[-1])
                
        
