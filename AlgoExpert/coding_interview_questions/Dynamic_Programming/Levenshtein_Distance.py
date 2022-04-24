'''
main idea: recursion + memo
time comp: O(mn)
space comp: O(mn)
- where n and m are the lengths of the two input strings
'''

def levenshteinDistance(str1, str2):
    # Write your code here.
	memo = {}
    def recr(str1, str2):
		n1 = len(str1)
		n2 = len(str2)
		
		if str1 == str2:
			return 0
		if n1 == 0:
			return len(str2)
		if n2 == 0:
			return len(str1)
		if str1[0] == str2[0]:
			return recr(str1[1:], str2[1:])
		
		if (str1, str2) not in memo:
			ret = float('inf')
			ret = min(
				recr(str1[1:], str2[1:]),
				recr(str1[1:], str2),
				recr(str1, str2[1:])
			)
			memo[str1, str2] = ret + 1
		return memo[str1, str2]
	
	return recr(str1, str2)
