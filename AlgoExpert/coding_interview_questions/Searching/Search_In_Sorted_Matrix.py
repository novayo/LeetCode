'''
main idea: greedy
time comp: O(H+W)
space comp: O(1)
- where H is the height of the input array and W is the width.
'''

def searchInSortedMatrix(matrix, target):
    # Write your code here.
	height = len(matrix)
	width = len(matrix[0])
	
    i, j = 0, width-1
	while 0 <= i < height and 0 <= j < width:
		val = matrix[i][j]
		
		if val > target:
			j -= 1
		elif val < target:
			i += 1
		else:
			return i, j
	return -1, -1
