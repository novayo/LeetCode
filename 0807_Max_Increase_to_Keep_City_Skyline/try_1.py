class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        # find maximum of each row and col
        col_info = collections.defaultdict(int)
        row_info = collections.defaultdict(int)
        for i in range(height):
            for j in range(width):
                col_info[i] = max(col_info[i], grid[i][j])
                row_info[j] = max(row_info[j], grid[i][j])
        
        
        # find min at each pos and calculate ans
        ans = 0
        for i in range(height):
            for j in range(width):
                ans += min(col_info[i], row_info[j]) - grid[i][j]
        
        return ans
