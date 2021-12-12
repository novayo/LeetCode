class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        從左、上出發，往大的找，並標記能走到的位置（True）
        再從右、下出發，往大的找，若走到的地方為(True)，即為答案 
        '''
        height = len(heights)
        width = len(heights[0])
        pacific_found = set()
        atlantic_found = set()
        
        def dfs(i, j, found, ans_found):
            if (i, j) in ans_found:
                ans.add((i, j))
                found.add((i, j))
            
            found.add((i, j))
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if x < 0 or y < 0 or x >= height or y >= width or (x, y) in found:
                    continue
                
                if heights[i][j] <= heights[x][y]:
                    dfs(x, y, found, ans_found)
            
        
        # pacific
        for i in range(height):
            dfs(i, 0, pacific_found, set())
        for j in range(width):
            dfs(0, j, pacific_found, set())
        
        
        # atlantic
        ans = set()
        for i in range(height):
            dfs(i, width-1, atlantic_found, pacific_found)
        for j in range(width):
            dfs(height-1, j, atlantic_found, pacific_found)
        
        return ans
                
