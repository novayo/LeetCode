'''
main idea: mark
time comp: O(N)
space comp: O(1)
- where N is the number of elements of the input array
'''
def removeIslands(matrix):
    # Write your code here.
	height = len(matrix)
	width = len(matrix[0])
	
	def dfs(i, j, marked):
		if not (0 <= i < height and 0 <= j < width) or matrix[i][j] == 0 or matrix[i][j] == marked:
			return
		
		matrix[i][j] = marked
		dfs(i+1, j, marked)
		dfs(i-1, j, marked)
		dfs(i, j+1, marked)
		dfs(i, j-1, marked)
		
	
	for i in range(height):
		if matrix[i][0] == 1:
			dfs(i, 0, -1)
		if matrix[i][width-1] == 1:
			dfs(i, width-1, -1)
	for j in range(width):
		if matrix[0][j] == 1:
			dfs(0, j, -1)
		if matrix[height-1][j] == 1:
			dfs(height-1, j, -1)
	
	
	for i in range(height):
		for j in range(width):
			if matrix[i][j] == 1:
				matrix[i][j] = 0
	
	for i in range(height):
		for j in range(width):
			if matrix[i][j] == -1:
				matrix[i][j] = 1
    return matrix

