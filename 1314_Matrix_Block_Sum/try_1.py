class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        
        def getElement(i, j, arr):
            if i < 0 or i >= height or j < 0 or j >= width:
                return 0
            else:
                return arr[i][j]
        
        # 先求出 每行的k個一組 [[-1,1,2], [1,2,3], ...]
        dp = copy.deepcopy(mat)
        for i in range(height):
            cur = 0
            for j in range(width):
                if j == 0:
                    cur = sum(mat[i][:k+1])
                    dp[i][j] = cur
                else:
                    cur += (getElement(i, j+k, mat) - getElement(i, j-k-1, mat))
                    dp[i][j] = cur
        
        # 計算 初始 k宮格 (row=0)  => dp[i-k] + ... dp[i+k] (超過範圍補0)
        ans = copy.deepcopy(dp)
        for j in range(width):
            for i in range(1, k+1):
                ans[0][j] += getElement(i, j, ans)
        
        # 每個宮格都是 上一宮格 - 上一宮格最上面那排 + 往下加一排
        for i in range(1, height):
            for j in range(width):
                ans[i][j] = getElement(i-1, j, ans) - getElement(i-k-1, j, dp) + getElement(i+k, j, dp)
        
        return ans