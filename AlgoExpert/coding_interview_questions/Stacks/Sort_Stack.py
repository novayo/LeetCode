'''
main idea: iteration
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''
def sortStack(stack):
    # Write your code here.
	new = []
    for _ in range(len(stack)):
		tmp = []
		cur_min = float('inf')
		
		while stack:
			a = stack.pop()
			cur_min = min(cur_min, a)
			tmp.append(a)
		
		while tmp:
			a = tmp.pop()
			if cur_min == a:
				new.append(a)
				cur_min = float('-inf')
			else:
				stack.append(a)
	
	return new

