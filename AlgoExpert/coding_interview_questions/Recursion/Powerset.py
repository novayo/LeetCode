'''
main idea: recursion
time comp: O(n*2^n)
space comp: O(n*2^n)
- where n is the length of the input array
'''
def powerset(array):
    # Write your code here.
	if not array:
		return [[]]
    
	def recr(idx):
		if idx >= len(array):
			return set([''])
		
		ret = set()
		for List in recr(idx+1):
			ret.add(tuple([array[idx]] + list(List)))
			ret.add(tuple(List))
		return ret
	
	return list(recr(0))
