'''
main idea: dp
time comp: O(HW)
space comp: O(HW)
- where H is the height of the matrix and W is the width
'''
def maximumSumSubmatrix(matrix, size):
    # Write your code here.
	height = len(matrix)
	width = len(matrix[0])
	
	dp = [[0] * (width+1) for _ in range(height+1)]
	
	dp[1][1] = matrix[0][0]
	for j in range(1, width):
		dp[1][j+1] = matrix[0][j] + dp[1][j]
		
	for i in range(1, height):
		dp[i+1][1] = matrix[i][0] + dp[i][1]
	
	for i in range(1, height):
		for j in range(1, width):
			dp[i+1][j+1] = matrix[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]
	
	
	ans = -float('inf')
	for i in range(size, height+1):
		for j in range(size, width+1):
			ans = max(
				ans,
				dp[i][j] - dp[i-size][j] - dp[i][j-size] + dp[i-size][j-size]
			)
	return ans

