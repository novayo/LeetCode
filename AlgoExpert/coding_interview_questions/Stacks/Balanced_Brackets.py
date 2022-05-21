'''
main idea: stack
time comp: O(n)
space comp: O(1)
- where n is the length of the input string
'''
def balancedBrackets(string):
    # Write your code here.
	pair = {')':'(', '}':'{', ']':'['}
	
    stack = []
	for s in string:
		if s in "({[":
			stack.append(s)
		elif s in pair:
			if not stack or stack[-1] != pair[s]:
				return False
			stack.pop()
	return len(stack) == 0
