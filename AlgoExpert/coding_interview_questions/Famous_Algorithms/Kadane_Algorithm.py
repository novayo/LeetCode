'''
main idea: kadane's algorithm
time comp: O(n)
space comp: O(1)
'''
def kadanesAlgorithm(array):
    # Write your code here.
    ans = s = array[0]
	for a in array[1:]:
		s = max(a, s+a)
		ans = max(ans, s)
	return ans

