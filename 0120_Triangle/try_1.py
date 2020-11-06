class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # 只能選 第(i+1, j) 與 (i+1, j+1)個
        memo = {}
        def recur(i, j, memo):
            if i >= len(triangle):
                return 0
            
            if (i, j) in memo:
                return memo[i, j]
            
            memo[i, j] = triangle[i][j] + min(recur(i+1, j, memo), recur(i+1, j+1, memo))
            
            return memo[i, j]
        
        return recur(0, 0, memo)
