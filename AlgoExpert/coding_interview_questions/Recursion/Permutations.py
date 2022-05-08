'''
main idea: recursion
time comp: O(n*n!)
space comp: O(n*n!)
- where n is the length of the input array
'''
def getPermutations(array):
    # Write your code here.
	if not array:
		return array
	ret = []
	
    def permutation(idx):
		if idx >= len(array):
			ret.append(array[:])
			return
		
		for i in range(idx, len(array)):
			array[i], array[idx] = array[idx], array[i]
			permutation(idx+1)
			array[i], array[idx] = array[idx], array[i]

	permutation(0)
	return ret
