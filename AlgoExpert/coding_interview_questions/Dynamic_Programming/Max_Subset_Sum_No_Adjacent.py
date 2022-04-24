'''
main idea: dp
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
'''
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
		return 0
	if len(array) <= 2:
		return max(array)
	
	a = array[0]
	b = array[1]
	c = a + array[2]
	
	for i in range(3, len(array)):
		d = array[i] + max(a, b)
		a = b
		b = c
		c = d
	
	return max(a, b, c)
