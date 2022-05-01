'''
main idea: check number of visited
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
'''

def hasSingleCycle(array):
    # Write your code here.
    idx = 0
	visited = 0
	
	while visited < len(array):
		if visited > 0 and idx == 0:
			return False
		idx = (idx + array[idx]) % len(array)
		visited += 1
		
	return idx == 0
