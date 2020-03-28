class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in matrix:
            if 0 in row:
                for i in range(len(row)):
                    if row[i] == 0:
                        row[i] = "-1"
                    else:
                        row[i] = 0

        for y in range(len(matrix[0])):
            for x in range(len(matrix)):
                if matrix[x][y] == "-1":
                    for _x in range(len(matrix)):
                        matrix[_x][y] = 0
                    break
