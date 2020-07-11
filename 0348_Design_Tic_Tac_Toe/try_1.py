class TicTacToe:
    '''
    一個move近來後，直接分別紀錄他的row, col, 跟斜對角
    如果有n個就表示贏了，輸出player
    '''
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.i = 0
        self.n = n
        self.players_row = [collections.defaultdict(list), collections.defaultdict(list)]
        self.players_col = [collections.defaultdict(list), collections.defaultdict(list)]
        self.players_diag = [collections.defaultdict(set), collections.defaultdict(set)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.i += 1
        # row
        self.players_row[player-1][row].append(col)
        if len(self.players_row[player-1][row]) == self.n:
            return player
        
        # col
        self.players_col[player-1][col].append(row)
        if len(self.players_col[player-1][col]) == self.n:
            return player
        
        # 右下斜角
        if row-col == 0:
            self.players_diag[player-1][row-col].add((row, col))
            if len(self.players_diag[player-1][row-col]) == self.n:
                return player
        
        # 左下斜角
        if row+col == self.n-1:
            self.players_diag[player-1][row+col].add((row, col))
            if len(self.players_diag[player-1][row+col]) == self.n:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
