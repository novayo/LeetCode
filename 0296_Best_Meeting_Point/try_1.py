class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        '''
        O(m*n) time / O(m + n) space
        - where m is the height of input 2d array and n is width.
        '''
        height = len(grid)
        width = len(grid[0])

        # get dp
        row_dp = [0] * width
        for j in range(width):
            if j > 0: row_dp[j] += row_dp[j-1]
            row_dp[j] += sum([grid[i][j] for i in range(height)])
        
        col_dp = [0] * height
        for i in range(height):
            if i > 0: col_dp[i] += col_dp[i-1]
            col_dp[i] += sum([grid[i][j] for j in range(width)])
        
        # get ans
        #   -- init first element
        dp = [0] * width
        num_of_one = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    num_of_one += 1
                    dp[0] += i + j
        
        #   -- init ans
        ans = dp[0]

        #   -- run first row 
        for j in range(1, width):
            dp[j] = dp[j-1] + 2 * row_dp[j-1] - num_of_one
            ans = min(ans, dp[j])
        
        #   -- run by col
        for i in range(1, height):
            for j in range(width):
                dp[j] = dp[j] + 2 * col_dp[i-1] - num_of_one
                ans = min(ans, dp[j])
        
        return ans