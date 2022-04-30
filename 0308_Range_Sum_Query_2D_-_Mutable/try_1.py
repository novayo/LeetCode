class BIT:
    def __init__(self, height, width):
        self.arr = [[0] * (width+1) for _ in range(height+1)]
        self.height = height+1
        self.width = width+1
    
    def update(self, x, y, delta):
        _x, _y = x, y
        while _x < self.height:
            while _y < self.width:
                self.arr[_x][_y] += delta
                _y += _y & -_y
            
            _x += _x & -_x
            _y = y
    
    def query(self, x, y):
        ret = 0
        
        _x, _y = x, y
        while _x > 0:
            while _y > 0:
                ret += self.arr[_x][_y]
                _y -= _y & -_y
            
            _x -= _x & -_x
            _y = y
        return ret
        
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.matrix = matrix
        self.tree = BIT(self.height, self.width)
        
        for i in range(self.height):
            for j in range(self.width):
                self.tree.update(i+1, j+1, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.tree.update(row+1, col+1, delta)
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.tree.query(row2+1, col2+1) \
               - self.tree.query(row2+1, col1) \
               - self.tree.query(row1, col2+1) \
               + self.tree.query(row1, col1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
