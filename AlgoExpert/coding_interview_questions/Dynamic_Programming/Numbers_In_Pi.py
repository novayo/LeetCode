'''
main idea: recursion
time comp: O(n^3 + m)
space comp: O(n + m)
- where n is the number of digits in Pi and m is the number of favorite numbers
'''

def numbersInPi(pi, numbers):
    # Write your code here.
    
	number_set = set(numbers)
	
	memo = {}
	def recr(start, end):
		if start >= len(pi):
			return 1
		
		if end >= len(pi):
			return float('inf')
		
		if (start, end) not in memo:
			ret = recr(start, end+1)
			if pi[start : end+1] in number_set:
				ret = min(ret, recr(end+1, end+1) + 1)
			memo[start, end] = ret
		return memo[start, end]
	
	ret = recr(0, 0)
	return ret - 2 if ret < float('inf') else -1