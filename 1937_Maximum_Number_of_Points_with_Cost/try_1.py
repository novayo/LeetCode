class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        dp 紀錄每列與上一列的到目前index的最大值（左邊與右邊）
        https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures.
        '''
        m = len(points)
        n = len(points[0])
        
        if m == 1: return max(points[0])
        if n == 1: return sum(sum(point) for point in points)
        
        def left(row):
            dp = [0] * n
            dp[0] = row[0]
            for i in range(1, n):
                dp[i] = max(dp[i-1]-1, row[i])
            return dp
        
        def right(row):
            dp = [0] * n
            dp[-1] = row[-1]
            for i in range(n-2, -1, -1):
                dp[i] = max(dp[i+1]-1, row[i])
            return dp
        
        ans = 0
        row = points[0]
        for i in range(m-1):
            l, r, cur = left(row), right(row), [0]*n
            for j in range(n):
                cur[j] = points[i+1][j] + max(l[j], r[j])
                ans = max(ans, cur[j])
            row = cur[:]
        return ans
