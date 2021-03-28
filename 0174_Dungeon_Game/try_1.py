class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 從end開始，看所需最少血量即可
        n = len(dungeon)
        m = len(dungeon[0])
        
        dp = {}
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                down = (i+1, j)
                right = (i, j+1)
                target = dungeon[i][j]
                
                if down not in dp and right not in dp:
                    dp[i, j] = abs(min(target, 0)) + 1
                elif down not in dp:
                    dp[i, j] = max(dp[right] + -target, 1)
                elif right not in dp:
                    dp[i, j] = max(dp[down] + -target, 1)
                else:
                    dp[i, j] = min(max(dp[right] + -target, 1), max(dp[down] + -target, 1))
                
        return dp[0, 0]