class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        把要改變的row 跟 col 先在最上跟最左記錄起來
        再把最上=0的行全改成0
        再把最左=0的列全改成0
        
        最後判斷[0][0]是否為0，更新最上跟最左為0
        如果原本最上或最左有0，也要更新最上為0或最左為0
        '''
        m = len(matrix)
        n = len(matrix[0])
        
        # 如果原本最上或最左有0，也要更新最上為0或最左為0
        first_ele_zero = matrix[0][0] == 0
        first_row_zero = False
        first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # 把要改變的row 跟 col 先在最上跟最左記錄起來
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 再把最上=0的行全改成0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        # 再把最左=0的列全改成0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
                    
        # 最後判斷[0][0]是否為0，更新最上跟最左為0
        if first_ele_zero:
            for i in range(m):
                matrix[i][0] = 0
            for j in range(n):
                matrix[0][j] = 0
        else:
            if first_col_zero:
                for i in range(m):
                    matrix[i][0] = 0
            if first_row_zero:
                for j in range(n):
                    matrix[0][j] = 0
