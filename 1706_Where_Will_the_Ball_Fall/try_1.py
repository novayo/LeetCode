class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        height = len(grid)
        width = len(grid[0])
        
        ans = []
        for j in range(width):
            
            for i in range(height):
                cur = grid[i][j]
                
                if cur == 1:
                    if j == width - 1 or grid[i][j+1] == -1:
                        break
                    i, j = i+1, j+1
                else:
                    if j == 0 or grid[i][j-1] == 1:
                        break
                    i, j = i+1, j-1
            
            if i >= height:
                ans.append(j)
            else:
                ans.append(-1)
        
        return ans