class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        遇到0，把相關的位置改成其他值，遇到0的時候跳過 => 先記錄要變成0的row col
        最後再把所有值改成0即可
        '''
        m = len(matrix)
        n = len(matrix[0])
        
        row_set = set()
        col_set = set()
        
        # 計算有哪些row col要變成0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(j)
                    col_set.add(i)
        
        # 將col全部變成0
        for col in col_set:
            for j in range(n):
                matrix[col][j] = 0
        
        # 將row全部變成0
        for i in range(m):
            for row in row_set:
                matrix[i][row] = 0
