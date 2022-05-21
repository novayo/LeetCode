'''
main idea: monotonic stack
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''
def nextGreaterElement(array):
    # Write your code here.
	ret = [-1] * len(array)
	
	stack = []
	for i, a in enumerate(array+array):
		while stack and stack[-1][0] < a:
			val, idx = stack.pop()
			ret[idx] = a
		stack.append((a, i%len(array)))
	
    return ret

