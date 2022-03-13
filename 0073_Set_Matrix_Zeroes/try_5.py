class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        1. if we encounter 0 => set matrix[0][y] = 0 and matrix[x][0] = 0
        2. looking for x=0 and y=0 to set its enitre row and column to 0's
        '''
        height = len(matrix)
        width = len(matrix[0])
        
        
        # mark first row and column
        if matrix[0][0] == 0:
            mark_x_0 = mark_0_y = True
        else:
            mark_x_0 = mark_0_y = False
        
        for i in range(1, height):
            if matrix[i][0] == 0:
                mark_x_0 = True
                
        for j in range(1, width):
            if matrix[0][j] == 0:
                mark_0_y = True
                

        # mark 0
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # replace 0
        for i in range(1, height):
            if matrix[i][0] == 0:
                for j in range(1, width):
                    matrix[i][j] = 0
        
        for j in range(1, width):
            if matrix[0][j] == 0:
                for i in range(1, height):
                    matrix[i][j] = 0
        
        # replace first row and column
        if mark_x_0:
            for i in range(height):
                matrix[i][0] = 0
        if mark_0_y:
            for j in range(width):
                matrix[0][j] = 0
        
                
        
