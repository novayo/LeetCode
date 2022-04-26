'''
main idea: check pre answer
time comp: O(n^2)
space comp: O(n^2)
- where n is the number of disks
'''
def diskStacking(disks):
    # Write your code here.
	dp = []
	
	disks.sort()
	for disk in disks:
		for i in range(len(dp)):
			if dp[i][-1][0] < disk[0] and dp[i][-1][1] < disk[1] and dp[i][-1][2] < disk[2]:
				dp[i].append(disk)
		dp.append([disk])
	
	ans = [-float('inf'), []]
	for d in dp:
		h = 0
		for _d in d:
			h += _d[-1]
		if h > ans[0]:
			ans = [h, d]
	return ans[1]