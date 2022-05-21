'''
main idea: stack
time comp: O(n)
space comp: O(n)
- where n is the length of input string
'''
def shortenPath(path):
    # Write your code here.
	stack = []
    for p in path.split('/'):
		if p == '..':
			if stack and stack[-1] != '..':
				stack.pop()
			elif path[0] != '/':
				stack.append(p)
		elif p == '.':
			continue
		elif p:
			stack.append(p)
	return '/' + '/'.join(stack) if path[0] == '/' else '/'.join(stack)
