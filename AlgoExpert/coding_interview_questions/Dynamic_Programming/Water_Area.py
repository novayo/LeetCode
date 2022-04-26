'''
main idea: prefix suffix dp
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''
def waterArea(heights):
    # Write your code here.
	if not heights:
		return 0
	
    n = len(heights)
	prefix = [heights[0]] * n
	suffix = [heights[-1]] * n
	
	# prefix
	cur = heights[0]
	for i in range(1, n):
		prefix[i] = cur
		cur = max(cur, heights[i])
	
	# suffix
	cur = heights[-1]
	for i in range(n-2, -1, -1):
		suffix[i] = cur
		cur = max(cur, heights[i])
	
	# loop
	ans = 0
	for i in range(n):
		if min(prefix[i], suffix[i]) - heights[i] > 0:
			ans += min(prefix[i], suffix[i]) - heights[i]
	return ans