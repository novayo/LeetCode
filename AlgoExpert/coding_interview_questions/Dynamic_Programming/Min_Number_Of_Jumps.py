'''
main idea: greedy
time comp: O(n)
space comp: O(1)
'''

def minNumberOfJumps(array):
    # Write your code here.
    cur_end = farest = 0
	ans = 0
	for i, v in enumerate(array[:-1]):
		farest = max(farest, i + v)
		if i == cur_end:
			cur_end = farest
			ans += 1
	return ans
