'''
main idea: dp
time comp: O(n^2)
space comp: O(n^2)
- where n is the length of the input array
'''
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    
	dp = set()
	for a in array:
		next_dp = set()
		next_dp.add((a,))
		for d in dp:
			next_dp.add(d)
			if d[-1] < a:
				next_dp.add(tuple(list(d) + [a]))
				
		dp = next_dp
	
	ans = [-float('inf'), []]
	for tup in dp:
		s = sum(tup)
		if s > ans[0]:
			ans = [s, list(tup)]
	return ans