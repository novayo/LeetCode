'''
main idea: brute force
time comp: O(n^4)
space comp: O(1)
'''
def squareOfZeroes(matrix):
    # Write your code here.
	height = len(matrix)
	width = len(matrix[0])
	
	for i in range(height):
		for j in range(width):
			if matrix[i][j] != 0:
				continue
				
			length = 2
			while i+length-1 < height and j+length-1 < width:
				r2, c2 = i+length-1, j+length-1
				if matrix[i][c2] != 0 or matrix[r2][j] != 0:
					break
				if isSquare(matrix, i, j, r2, c2):
					return True
				length += 1
	return False

def isSquare(matrix, r1, c1, r2, c2):
	for i in range(r1, r2+1):
		if matrix[i][c1] != 0 or matrix[i][c2] != 0:
			return False
	for j in range(c1, c2+1):
		if matrix[r1][j] != 0 or matrix[r2][j] != 0:
			return False
	return True
