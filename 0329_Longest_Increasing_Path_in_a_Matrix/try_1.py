class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp= {(x, y): longest path}
        height = len(matrix)
        width = len(matrix[0])
        
        def recr(x, y, memo, found):
            found.add((x, y))
            
            ans = 1
            for _x, _y in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                # 若不符合規則，就跳過
                if _x < 0 or _y< 0 or _x >= height or _y >= width or matrix[x][y] >= matrix[_x][_y]:
                    continue
                
                # 若符合規則 且 有找過了 => 取用找過的資料
                if (_x, _y) in memo:
                    ans = max(ans, memo[_x, _y] + 1)
                    continue
                
                # 不能回頭找
                if (_x, _y) in found:
                    continue
                    
                ans = max(ans, recr(_x, _y, memo, found)+1)
            
            memo[x, y] = ans
            return memo[x, y]
        
        ans = 0
        dp = {}
        for x in range(height):
            for y in range(width):
                ans = max(ans, recr(x, y, dp, set()))
        return ans