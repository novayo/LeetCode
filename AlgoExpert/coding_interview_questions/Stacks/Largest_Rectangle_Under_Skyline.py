'''
main idea: stack
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
	ans = 0
	stack = [[-1,-1]]
	for i, height in enumerate(buildings):
		while stack[-1] != -1 and stack[-1][0] > height:
			val, idx = stack.pop()
			ans = max(ans, (i-idx) * val)
		
		stack.append((height, i))
	
	while stack[-1][1] != -1:
		val, idx = stack.pop()
		ans = max(ans, (len(buildings)-stack[-1][1]-1) * val)
    return ans

