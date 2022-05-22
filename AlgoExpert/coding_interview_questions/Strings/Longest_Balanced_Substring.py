'''
main idea: marked
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''
def longestBalancedSubstring(string):
    # Write your code here.
	n = len(string)
    marked = [False] * n
	
	stack = []
	for i, s in enumerate(string):
		if s == '(':
			stack.append(i)
		elif stack:
			j = stack.pop()
			marked[i] = marked[j] = True
	
	ans = 0
	cur = 0
	for i in range(n):
		if marked[i]:
			cur += 1
		else:
			cur = 0
		
		ans = max(ans, cur)
	return ans
