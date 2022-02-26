class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''
        k = 0 => 1*1
        k = 1 => 3*3
        k = 2 => 5*5
        
        presum
        '''
        def get(i, j, arr):
            if i < 0 or j < 0 or i >= height or j >= width:
                return 0
            return arr[i][j]
        
        height = len(mat)
        width = len(mat[0])
        
        # presum
        row_k_sum = [[0] * width for _ in range(height)]
        for i in range(height):
            cur_sum = 0
            for j in range(width):
                if j == 0:
                    cur_sum = sum(mat[i][:k+1])
                else:
                    cur_sum += get(i, j+k, mat) - get(i, j-k-1, mat)
                row_k_sum[i][j] = cur_sum
        
        # init
        dp = copy.deepcopy(row_k_sum)
        for j in range(width):
            for i in range(1, k+1):
                dp[0][j] += get(i, j, row_k_sum)
        
        # move down
        for i in range(1, height):
            for j in range(width):
                dp[i][j] = dp[i-1][j] + get(i+k, j, row_k_sum) - get(i-k-1, j, row_k_sum)
        
        return dp
