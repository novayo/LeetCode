'''
main idea: dfs + memo
time comp: O(low * high * n)
space comp: O(low * high)
- where n is the length of the input array
'''

def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
	measuringCups.sort(reverse=True)
	
	memo = set()
	def dfs(l, r):
		if low <= l and r <= high:
			return True
		
		if r > high:
			return False
		
		if (l, r) not in memo:
			memo.add((l, r))
			for a, b in measuringCups:
				if dfs(l+a, r+b):
					return True
		return False
	
    return dfs(0, 0)
