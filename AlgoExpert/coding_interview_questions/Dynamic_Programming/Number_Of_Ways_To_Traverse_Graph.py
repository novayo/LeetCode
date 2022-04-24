'''
main idea: dp
time comp: O(hw)
space comp: O(w)
- where h is the height of the graph and w is the width.
'''
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
	dp = [1] * (width+1)
	for i in range(1, height):
		for j in range(1, width+1):
			dp[j] += dp[j-1]
    return dp[-2]

