'''
main idea: backtracking
time comp: O(9^3)
space comp: O(9^2)
'''
def solveSudoku(board):
    # Write your code here.
	
	rows = [set() for _ in range(9)]
	cols = [set() for _ in range(9)]
	blocks = [set() for _ in range(9)]
	
	# init
	for i in range(9):
		for j in range(9):
			if board[i][j] != 0:
				rows[i].add(board[i][j])
				cols[j].add(board[i][j])
				blocks[i//3*3 + j//3].add(board[i][j])
	
	def dfs(i, j):
		if j >= 9:
			i, j = i+1, 0
		
		if i >= 9:
			return True
		
		if board[i][j] == 0:
			for k in range(1, 9+1):
				if k in rows[i] or k in cols[j] or k in blocks[i//3*3 + j//3]:
					continue
				board[i][j] = k
				rows[i].add(k)
				cols[j].add(k)
				blocks[i//3*3 + j//3].add(k)
				
				if dfs(i, j+1):
					return True
				
				board[i][j] = 0
				rows[i].remove(k)
				cols[j].remove(k)
				blocks[i//3*3 + j//3].remove(k)
		else:
			if dfs(i, j+1):
				return True
		
		return False
	
	dfs(0, 0)
    return board
