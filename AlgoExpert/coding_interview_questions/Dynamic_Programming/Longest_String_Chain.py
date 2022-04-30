'''
main idea: dfs + memo
time comp: O(n * m^2 + nlogn)
space comp: O(nm)
- where n is the number of strings and m is the length of the longest string
'''
def longestStringChain(strings):
    # Write your code here.
    string_set = set(strings)
	strings.sort(key=len, reverse=True)
	
	memo = {}
	def dfs(string):
		if string == '' or string not in string_set:
			return []
		
		if string not in memo:
			ret = []
			for i in range(len(string)):
				r = dfs(string[:i] + string[i+1:])
				if len(ret) < len(r):
					ret = r
			memo[string] = [string] + ret
		return memo[string]
	
	
	ret = []
	for s in strings:
		r = dfs(s)
		if len(ret) < len(r):
			ret = r
	return ret if len(ret) > 1 else []
	
	
