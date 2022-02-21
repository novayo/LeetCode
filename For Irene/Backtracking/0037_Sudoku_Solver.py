class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 我需要嘗試所有的"."的位置 => 要如何知道填入 1 是不是valid? => 先找出目前的數字，用36的方法存起來
        # O(n)
        col_set = [set() for i in range(9)]
        row_set = [set() for i in range(9)]
        block_set = [set() for i in range(9)]
        
        for x in range(9):
            for y in range(9):
                # 不跑"."
                if board[x][y] == ".":
                    continue
                
                # 數字塞入對應set
                col_set[x].add(board[x][y])
                row_set[y].add(board[x][y])
                block_set[x//3*3+y//3].add(board[x][y])
        
        # recursive -> backtracking
        def backtracking(x, y):
            if y >= 9:
                x = x+1
                y = 0
                
            if x >= 9:
                return True
            
            # 如果 (x,y) => "." => 嘗試填入 "1"~"9"
            if board[x][y] == '.':
                for attempt in range(1, 9+1):
                    # 轉成string
                    attempt = str(attempt)
                    
                    # 看是否合理 => 如果合理 改變board 且 加入set
                    if (attempt in col_set[x]) or (attempt in row_set[y]) or (attempt in block_set[x//3*3+y//3]):
                        continue
                    else:
                        board[x][y] = attempt
                        col_set[x].add(attempt)
                        row_set[y].add(attempt)
                        block_set[x//3*3+y//3].add(attempt)
                    
                    
                    # 繼續下一輪嘗試
                    if backtracking(x, y+1):
                        return True
                    
                    # 回到加入set前的狀態 => 刪除set
                    board[x][y] = "."
                    col_set[x].remove(attempt)
                    row_set[y].remove(attempt)
                    block_set[x//3*3+y//3].remove(attempt)
            
            else:
                # 繼續下一輪嘗試
                if backtracking(x, y+1):
                    return True
            
            return False
    
        backtracking(0, 0)