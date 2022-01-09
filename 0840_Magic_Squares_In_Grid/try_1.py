class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        '''
        brute force
        '''
        
        height = len(grid)
        width = len(grid[0])
        
        def isMagic_Square(i, j):
            # check length
            if i+2 >= height or j+2 >= width:
                return False
            
            # check number and calculate all row and col and diag.
            row_dict = collections.defaultdict(int)
            col_dict = collections.defaultdict(int)
            all_number = set()
            
            for _i in range(i, i+3):
                for _j in range(j, j+3):
                    number = grid[_i][_j]
                    
                    if not (0 < number < 10):
                        return False
                    all_number.add(number)
                    row_dict[_i] += number
                    col_dict[_j] += number
            
                        
            diag = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            anti_diag = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
            
            if len(all_number) != 9 \
               or len(set(row_dict.values())) > 1 \
               or len(set(col_dict.values())) > 1 \
               or not (diag == anti_diag == list(row_dict.values())[0] == list(col_dict.values())[0]):
                return False
            else:
                return True
        
        ans = 0
        for i in range(height):
            for j in range(width):
                if isMagic_Square(i, j):
                    ans += 1
        return ans