class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        
        for row in matrix:
            i=0
            zero_in_row = False
            while i<len(row):
                if row[i] == 0:
                    cols.add(i)
                    if zero_in_row == False:
                        zero_in_row = True
                        i = 0
                        continue
                if zero_in_row:
                    row[i] = 0
                i += 1
                
        for row in matrix:
            for c in cols:
                row[c] = 0
        
        
