'''
main idea: dfs
time comp: O(N)
space comp: O(N)
- where N is the number of elements of the input matrix
'''

def riverSizes(matrix):
    # Write your code here.
	height = len(matrix)
	width = len(matrix[0])
	
	def dfs(i, j):
		if not (0 <= i < height and 0 <= j < width) or matrix[i][j] == 0:
			return 0
		matrix[i][j] = 0
		return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
	
	ans = []
	for i in range(height):
		for j in range(width):
			if matrix[i][j] == 1:
				ans.append(dfs(i, j))
	return ans
