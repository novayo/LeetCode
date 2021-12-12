class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        只能夠確認一點
            - 用dfs去確認
            - 紀錄 True or False
        下一點遇到的就可以直接回傳了，只找沒找過的點
        
        從大的開始找 => 減枝
        '''
        height = len(heights)
        width = len(heights[0])
        
        # -1: 每找過, 0: False, 1: True
        dp = [[-1 for _ in range(width)] for __ in range(height)]

        # define loop order
        mapping = collections.defaultdict(list)
        for i in range(height):
            for j in range(width):
                target = heights[i][j]
                mapping[target].append((i, j))
        
        # define dfs
        def dfs(i, j, ans, found):
            
            if i == 0 or j == 0:
                ans[0] = True
            if i == height-1 or j == width-1:
                ans[1] = True
                
            if dp[i][j] == 0:
                return
            elif dp[i][j] == 1:
                ans[0] = ans[1] = True
                return
        
            if ans[0] and ans[1]:
                return
        
            target = heights[i][j]
            found.add((i, j))
        
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if x < 0 or y < 0 or x >= height or y >= width or (x, y) in found:
                    continue
                
                neighbor = heights[x][y]
                if target >= neighbor:
                    dfs(x, y, ans, found)
        
        # loop
        ans = []
        
        for key in sorted(mapping.keys(), reverse=True):
            nodes = mapping[key]
            
            for i, j in nodes:
                tmp = [False, False]
                dfs(i, j, tmp, set())
                
                if tmp[0] and tmp[1]:
                    dp[i][j] = 1
                    ans.append([i, j])
                else:
                    dp[i][j] = 0

        return ans
        
