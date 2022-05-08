'''
main idea: recursion
time comp: O(n)
space comp: O(d)
- where n is the total number of elements in the array and d is the greatest depth of "special" arrays in the array
'''
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    
	def recr(array, depth=1):
		ret = 0
		for a in array:
			if isinstance(a, int):
				ret += depth * a
			else:
				ret += depth * recr(a, depth+1)
		return ret
	return recr(array)
