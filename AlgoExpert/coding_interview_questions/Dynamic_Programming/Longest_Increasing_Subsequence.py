'''
main idea: patient sort
time comp: O(nlogn)
space comp: O(n)
- where n is the length of the input array
'''

import bisect

def longestIncreasingSubsequence(array):
    # Write your code here.
    path_index = []
	dp = []
	for i, a in enumerate(array):
		idx = bisect.bisect_left(dp, [a,])
		
		if idx >= len(dp):
			path_index.append(-1 if not dp else dp[-1][1])
			dp.append([a, i])
		else:
			path_index.append(-1 if idx==0 else dp[idx-1][1])
			dp[idx] = [a, i]
			
	ans = []
	t = dp[-1][1]
	while t >= 0:
		ans.append(array[t])
		t = path_index[t]
	return ans[::-1]
	
