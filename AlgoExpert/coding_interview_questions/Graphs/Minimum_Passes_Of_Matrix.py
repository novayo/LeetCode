'''
main idea: bfs
time comp: O(N)
space comp: O(N)
- where N is the number of elements of the input array
'''
def minimumPassesOfMatrix(matrix):
    # Write your code here.
	height = len(matrix)
	width = len(matrix[0])
	
	queue = set()
	for i in range(height):
		for j in range(width):
			if matrix[i][j] > 0:
				queue.add((i, j))
	
	layer = -1
	while queue:
		next_queue = set()
		layer += 1
		for i, j in queue:
			for x, y in [i-1, j], [i+1, j], [i, j+1], [i, j-1]:
				if not (0 <= x < height and 0 <= y < width) or matrix[x][y] >= 0:
					continue
				matrix[x][y] *= -1
				next_queue.add((x, y))
		queue = next_queue
    
	for i in range(height):
		for j in range(width):
			if matrix[i][j] < 0:
				return -1
	return layer

