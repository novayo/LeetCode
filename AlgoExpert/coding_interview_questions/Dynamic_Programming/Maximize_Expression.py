'''
main idea: prefix
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''
def maximizeExpression(array):
    # Write your code here.
	n = len(array)
	
	if n < 4:
		return 0
	
	# a
	dp = [0] * n
	cur_max = -float('inf')
	for i in range(n):
		cur_max = max(cur_max, array[i])
		dp[i] = cur_max
	
	# a-b
	dp1 = [0] * n
	cur_max = -float('inf')
	for i in range(1, n):
		cur_max = max(cur_max, dp[i-1] - array[i])
		dp1[i] = cur_max
	
	# a-b+c
	dp2 = [0] * n
	cur_max = -float('inf')
	for i in range(2, n):
		cur_max = max(cur_max, dp1[i-1] + array[i])
		dp2[i] = cur_max
	
	# a-b+c-d
	dp3 = [0] * n
	cur_max = -float('inf')
	for i in range(3, n):
		cur_max = max(cur_max, dp2[i-1] - array[i])
		dp3[i] = cur_max
	
	return dp3[-1]