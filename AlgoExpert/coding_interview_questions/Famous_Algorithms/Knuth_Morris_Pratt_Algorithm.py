'''
main idea: KMP
time comp: O(N+M)
space comp: O(M)
- where N is the length of the string and M is the length of the substring
'''
def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
    pattern = buildPattern(substring)
	return isMatch(string, substring, pattern)

def buildPattern(string):
	pattern = [-1] * len(string)
	i, j = 0, 1
	while j < len(string):
		if string[i] == string[j]:
			pattern[j] = i
			i += 1
			j += 1
		elif i > 0:
			i = pattern[i-1] + 1
		else:
			j += 1
	return pattern

def isMatch(string, substring, pattern):
	i, j = 0, 0
	while i < len(string) and j < len(substring):
		if string[i] == substring[j]:
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j-1] + 1
		else:
			i += 1
	return j >= len(substring)
