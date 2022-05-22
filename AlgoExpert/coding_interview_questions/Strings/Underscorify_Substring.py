'''
main idea: merge interval
time comp: O(nm)
space comp: O(n)
- where n is the length of the main string and m is the length of the substring
'''
def underscorifySubstring(string, substring):
    # Write your code here.
	n = len(string)
	m = len(substring)
    matches = []
	for i in range(n-m+1):
		if string[i:i+m] == substring:
			if matches and matches[-1][1] >= i:
				matches[-1][1] = i+m
			else:
				matches.append([i, i+m])
	
	for a, b in matches[::-1]:
		string = string[:a] + '_' + string[a:b] + '_' + string[b:]
	return string
