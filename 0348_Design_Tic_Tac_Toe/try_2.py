class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = collections.defaultdict(lambda: collections.defaultdict(int))
        self.col = collections.defaultdict(lambda: collections.defaultdict(int))
        self.diag = collections.defaultdict(lambda: collections.defaultdict(int))
        self.anti_diag = collections.defaultdict(lambda: collections.defaultdict(int))

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row][player] += 1
        self.col[col][player] += 1
        self.diag[row+col][player] += 1
        self.anti_diag[row-col][player] += 1
        
        if self.row[row][player] == self.n or \
           self.col[col][player] == self.n or \
           self.diag[row+col][player] == self.n or \
           self.anti_diag[row-col][player] == self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
