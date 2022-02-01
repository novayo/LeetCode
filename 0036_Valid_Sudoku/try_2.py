class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                target = board[i][j]
                box_index = i//3*3+j//3
                
                if target == '.':
                    continue
                    
                if target in row_set[i] \
                   or target in col_set[j] \
                   or target in box_set[box_index]:
                    return False
                
                row_set[i].add(target)
                col_set[j].add(target)
                box_set[box_index].add(target)
        
        return True
