class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        
        # get presum
        presum = [[0] * (width+1) for _ in range(height+1)]
        for i in range(1, height+1):
            for j in range(1, width+1):
                presum[i][j] = grid[i-1][j-1] + presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1]  

        # get answer
        ans = 0
        for i in range(height-3+1):
            for j in range(width-3+1):
                ans = max(ans, presum[i+3][j+3] - presum[i+3][j] - presum[i][j+3] + presum[i][j] - grid[i+1][j] - grid[i+1][j+2])
        
        return ans
        