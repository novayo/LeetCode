class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        column = [set() for _ in range(9)]
        box = [set() for _ in range(3)]
        
        for index_row, rowb in enumerate(board):
            for index_digit, digit in enumerate(rowb):
                if digit == '.': continue
                if digit in row or digit in column[index_digit] or digit in box[index_digit//3]:
                    return False
                else:
                    row.add(digit)
                    column[index_digit].add(digit)
                    box[index_digit//3].add(digit)
            row.clear()
            if index_row%3 == 2:
                box[0].clear()
                box[1].clear()
                box[2].clear()
        
        return True
