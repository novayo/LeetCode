class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def getFromDp(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            return mat[i][j]
            
        m, n = len(mat), len(mat[0])
        
        # init
        for i in range(1, m):
            mat[i][0] += mat[i-1][0]
        
        for j in range(1, n):
            mat[0][j] += mat[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        
        # get answer
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                left_top = [i-k, j-k]
                left_down = [min(i+k, m-1), j-k]
                right_top = [i-k, min(j+k, n-1)]
                right_down = [min(i+k, m-1), min(j+k, n-1)]
                
                ans[i][j] = getFromDp(right_down[0], right_down[1]) \
                    - getFromDp(right_top[0]-1, right_top[1]) \
                    - getFromDp(left_down[0], left_down[1]-1) \
                    + getFromDp(left_top[0]-1, left_top[1]-1)
        return ans
                
